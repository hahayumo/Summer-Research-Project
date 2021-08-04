import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from random import randrange
from numpy.random import RandomState
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import adfuller
from scipy import signal
from scipy import stats
from statsmodels.tsa.api import VAR
from statsmodels.tools.eval_measures import rmse, aic
import pickle
from statsmodels.stats.stattools import durbin_watson
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.stattools import grangercausalitytests
from scipy.optimize import minimize
import rpy2
from rpy2.robjects.packages import importr
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
import datetime
from rpy2.robjects.vectors import FloatVector

np.random.seed(9868)
yuima = importr("yuima")
n_ou_sim_string = """
n_sim_ou = function(random_seed, num_sim,
                    mu11, mu12, mu21, mu22,
                    sigma11, sigma12, sigma21, sigma22,
                    xinit, T0, T, length){
  
  set.seed(random_seed)
  
  drift = c("mu11-mu12*X1", "mu21-mu22*X2")
  diffusion = matrix(c("sigma11", "sigma12", "sigma21", "sigma22"), 2, 2, byrow=TRUE)
  ou_model = setModel(drift=drift, diffusion=diffusion, 
                        time.variable = "t",
                        state.var=c("X1","X2"), solve.variable=c("X1","X2"))
  
  newsamp = setSampling(Initial=T0, Terminal=T, n=length)
  
  n_sim_ou_data = data.frame(matrix(nrow=length+1, ncol=2*num_sim))
  for (i in 1:num_sim){
    ou_sim = simulate(ou_model, 
                      true.par=list(
                        mu11=mu11, mu12=mu12, mu21=mu21, mu22=mu22, 
                        sigma11=sigma11, sigma12=sigma12, sigma21=sigma21, sigma22=sigma22), 
                      xinit=xinit, sampling=newsamp)
    original_data = ou_sim@data@original.data
    one_sim_ou = data.frame(original_data[,1], original_data[,2])
    colnames(one_sim_ou) = c('series1', 'series2')
    n_sim_ou_data[, (2*i-1):(2*i)] = one_sim_ou
  }
  return(n_sim_ou_data)
}
"""
n_ou_sim = SignatureTranslatedAnonymousPackage(n_ou_sim_string, "n_ou_sim")
def n_ou_simulation(random_seed, num_sim,
                    mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22,
                    xinit, T0, T, length):
    """n simulation of bivariate Ornstein-Uhlenbeck model,
    length = length of one series
    checked
    """
    n_ou_sim_data = pd.DataFrame(
        n_ou_sim.n_sim_ou(random_seed=random_seed, num_sim=num_sim,
                              mu11=mu11, mu12=mu12, mu21=mu21, mu22=mu22,
                              sigma11=sigma11, sigma12=sigma12, sigma21=sigma21, sigma22=sigma22,
                              xinit=xinit, T0=T0, T=T, length=length)).transpose()
    return n_ou_sim_data

def price_to_log_price(n_price):

    """checked"""
    return(np.log(n_price))
def log_price_to_price(n_log_price):

    """checked"""
    return(np.exp(n_log_price))
def price_to_return(n_price):
    """checked"""

    n_return = pd.DataFrame()
    for i in range(n_price.shape[1]):
        ith_column_price_series = n_price.iloc[:, i]
        n_return = pd.concat([n_return, 100 * np.log(ith_column_price_series[1:].values / ith_column_price_series[:-1])], axis=1)
    return n_return
def log_price_to_return(n_log_price):
    """checked"""

    n_real_return = pd.DataFrame()
    for i in range(n_log_price.shape[1]):
        ith_column_price_series = n_log_price.iloc[:, i]
        n_real_return = pd.concat([n_real_return, 100 * (ith_column_price_series[1:].values - ith_column_price_series[:-1])], axis=1)
    return n_real_return
def cal_stats(n_return, n_price=None):
    """ 'mean' and 'sd' checked
    'skewness' and 'kurtosis' checked
    (different expressions of calculation from intro to stat finance)
    8 statistics
    """

    return_series1 = n_return.iloc[:, ::2]
    return_series2 = n_return.iloc[:, 1::2]

    mean1 = return_series1.mean(axis=0).values
    sd1 = return_series1.std(axis=0).values
    skew1 = return_series1.skew(axis=0).values
    kurtosis1 = return_series1.kurtosis(axis=0).values

    mean2 = return_series2.mean(axis=0).values
    sd2 = return_series2.std(axis=0).values
    skew2 = return_series2.skew(axis=0).values
    kurtosis2 = return_series2.kurtosis(axis=0).values

    stats_data = pd.DataFrame([mean1, mean2, sd1, sd2, skew1, skew2, kurtosis1, kurtosis2])
    stats_data = stats_data.transpose()
    stats_data.columns = [
        'return_mean1', 'return_mean2',
        'return_sd1', 'return_sd2',
        'return_skew1', 'return_skew2',
        'return_kurtosis1', 'return_kurtosis2']
    return stats_data
def loss_function(params):
    """n_real_stats is a global amount calculated outside the function"""

    params = FloatVector(params)
    """ moment_loss checked """
    moment_loss = pd.DataFrame().reindex_like(n_real_stats)
    """ checked: each time calling the function, different randseed can be generated;
    but with a np.random.seed, each time running the whole parts, the results of randseeds are the same
    """

    randseed = np.random.randint(low=0, high=1000000, size=(1,))

    n_sim_log_price = n_ou_simulation(
        random_seed=int(randseed), num_sim=num_sim,
        mu11=params[0], mu12=params[1], mu21=params[2], mu22=params[3],
        sigma11=params[4], sigma12=params[5], sigma21=params[6], sigma22=params[7],
        xinit=xinit, T0=T0, T=T, length=length)

    n_sim_price = log_price_to_price(n_sim_log_price)
    n_sim_return = price_to_return(n_sim_price)
    n_sim_stats = cal_stats(n_sim_return)

    for i in range(n_real_stats.shape[0]):
        for j in range(n_real_stats.shape[1]):
            moment_loss.iloc[i, j] = np.sqrt((n_real_stats.iloc[i, j] - n_sim_stats.iloc[i, j])**2)

    """ sum_all checked """
    sum_all = np.sum(moment_loss)
    # moments_max = np.max(moment_loss)
    # losses = sum_all / moments_max
    return np.sum(sum_all)


n_real_price = pd.read_csv("/Users/changmao/Desktop/real_pair_prices.csv", index_col=[0])
n_real_log_price = price_to_log_price(n_real_price)

n_real_return = pd.read_csv("/Users/changmao/Desktop/real_pair_returns.csv", index_col=[0])
n_real_stats = cal_stats(n_return=n_real_return, n_price=None)


""" fixed constants:
"""
random_seed = 9868
xinit = [2, 3]
num_sim, T0, T, length = n_real_stats.shape[0], 0, 1, n_real_price.shape[0]

""" 8 params are
"""
# mu11, mu12, mu21, mu22 = 5, 0.7, 4.5, 0.6
# sigma11, sigma12, sigma21, sigma22 = 0.5, 2, 1.5, 0.7


""" checked: same minimisation results """
np.random.seed(9868)
begin_time1 = datetime.datetime.now()
initial0 = [1, 1, 1, 1, 1, 1, 1, 1]
res1 = minimize(loss_function, initial0, method='Powell', tol=1e-6, options={'disp': True})
time1 = datetime.datetime.now() - begin_time1
print(time1)
print(res1.x)
# options={'disp': True, 'maxiter': 200}







params = (res1.x)
params = FloatVector(params)
moment_loss = pd.DataFrame().reindex_like(n_real_stats)
randseed = np.random.randint(low=0, high=1000000, size=(1,))

n_sim_log_price = n_ou_simulation(
    random_seed=int(randseed), num_sim=num_sim,
    mu11=params[0], mu12=params[1], mu21=params[2], mu22=params[3],
    sigma11=params[4], sigma12=params[5], sigma21=params[6], sigma22=params[7],
    xinit=xinit, T0=T0, T=T, length=length)

n_sim_price = log_price_to_price(n_sim_log_price)
n_sim_return = price_to_return(n_sim_price)
n_sim_stats = cal_stats(n_sim_return)

for i in range(n_real_stats.shape[0]):
    for j in range(n_real_stats.shape[1]):
        moment_loss.iloc[i, j] = np.sqrt((n_real_stats.iloc[i, j] - n_sim_stats.iloc[i, j])**2)

sum_all = np.sum(moment_loss)
print(sum_all)