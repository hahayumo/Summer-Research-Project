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
# --------------------------------------------------------------------------------
np.random.seed(123)
yuima = importr("yuima")
one_bjd_sim_string = """
one_sim_jump_diff = function(
  theta11 = 10, theta12 = 1, theta21 = 10, theta22=1, 
  p1 = 2, p2 = 0.5, p3 = 1, p4 = 1, 
  j1 = 1, j2 =   2, j3 = 4, j4 = 1,
  x0=c(2,3), random_seed=9868){

  set.seed(random_seed)
  a = c("theta11*t-theta12*X1", "theta21*t-theta22*X2")
  b = matrix(c("p1","p2","p3","p4"), 2, 2, byrow=TRUE)
  c = matrix(c("j1", "j2", "j3", "j4"), 2, 2, byrow=TRUE) 

  alpha = 2
  beta = c(0, 0)
  delta0 = 0.55
  mu = c(0,0)
  Lambda = matrix(c(1,0,0,1), 2, 2)

  model = setModel(drift=a, xinit=x0, diffusion=b, 
                        jump.coeff=c, measure.type="code", 
                        measure=list(df="rNIG(z, alpha, beta, delta0, mu, Lambda)"), 
                        state.variable=c("X1","X2"), 
                        solve.variable=c("X1","X2"))

  samp = setSampling(Terminal=1, n=200)
  yuima = setYuima(model=model, sampling=samp) 
  sim = simulate(yuima, 
                 true.par=list(alpha=alpha, beta=beta, delta0=delta0, mu=mu, Lambda=Lambda, 
                               theta11=theta11, theta12=theta12, theta21=theta21, theta22=theta22, 
                               p1=p1, p2=p2, p3=p3, p4=p4, 
                               j1=j1, j2=j2, j3=j3, j4=j4))
  one_sim_bi_jump_diff = data.frame(sim@data@original.data)
  return(one_sim_bi_jump_diff)
}
"""
one_bjd_sim = SignatureTranslatedAnonymousPackage(one_bjd_sim_string, "one_bjd_sim")
# --------------------------------------------------------------------------------
def one_bjd_simulation(theta11=5, theta12=2, theta21=5, theta22=2, p1=2, p2=0.5, p3=1, p4=1, j1=1, j2=2, j3=4, j4=1, x0=[2, 4], random_seed=9868):
    """one simulation of bivariate jump diffusion model
    T=1, length of one series = 200
    """
    one_bjd_sim_data = pd.DataFrame(
        one_bjd_sim.one_sim_jump_diff(
            theta11=theta11, theta12=theta12, theta21=theta21, theta22=theta22,
            p1=p1, p2=p2, p3=p3, p4=p4, j1=j1, j2=j2, j3=j3, j4=j4,
            x0=x0, random_seed=random_seed)).transpose()
    return one_bjd_sim_data
def n_bjd_simulation(random_seed, theta11=5, theta12=1, theta21=5, theta22=1, p1=2, p2=0.5, p3=1, p4=1, j1=1, j2=0.5, j3=1, j4=1, x0=[2, 4], n_sim=248):
    """ n simulation of bivariate jump diffusion model """
    """ random_seed: a vector of random numbers in (0, 100000) """
    n_bjd_sim_data = pd.DataFrame()
    for i in range(n_sim):
        one_bjd_sim_data = one_bjd_simulation(
            theta11=theta11, theta12=theta12, theta21=theta21, theta22=theta22,
            p1=p1, p2=p2, p3=p3, p4=p4, j1=j1, j2=j2, j3=j3, j4=j4,
            x0=x0, random_seed=int(random_seed[i]))
        n_bjd_sim_data = pd.concat([n_bjd_sim_data, one_bjd_sim_data], axis=1)
    return n_bjd_sim_data
def price_to_log_price(n_price):
    return(np.log(n_price))
def log_price_to_price(n_log_price):
    return(np.exp(n_log_price))
def price_to_return(n_price):

    n_return = pd.DataFrame()
    for i in range(n_price.shape[1]):
        ith_column_price_series = n_price.iloc[:, i]
        n_return = pd.concat([n_return, 100 * np.log(ith_column_price_series[1:].values / ith_column_price_series[:-1])], axis=1)
    return n_return
def log_price_to_return(n_log_price):
    n_real_return = pd.DataFrame()
    for i in range(n_log_price.shape[1]):
        ith_column_price_series = n_log_price.iloc[:, i]
        n_real_return = pd.concat([n_real_return, 100 * (ith_column_price_series[1:].values - ith_column_price_series[:-1])], axis=1)
    return n_real_return
def cal_stats(n_return, n_price=None):

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

    params = FloatVector(params)
    moment_loss = pd.DataFrame().reindex_like(n_real_stats)

    randseed2 = np.random.randint(low=0, high=1000000, size=(num_sim,))
    n_sim_log_price = n_bjd_simulation(
        random_seed=randseed2,
        theta11=params[0], theta12=theta12, theta21=params[1], theta22=theta22,
        p1=params[2], p2=p2, p3=p3, p4=params[3], j1=j1, j2=j2, j3=j3, j4=j4,
        x0=x0, n_sim=num_sim)
    n_sim_price = log_price_to_price(n_sim_log_price)
    n_sim_return = price_to_return(n_sim_price)
    n_sim_stats = cal_stats(n_sim_return)

    for i in range(n_real_stats.shape[0]):
        for j in range(n_real_stats.shape[1]):
            moment_loss.iloc[i, j] = np.sqrt((n_real_stats.iloc[i, j] - n_sim_stats.iloc[i, j])**2)

    sum_all = np.sum(moment_loss)
    return np.sum(sum_all)
# --------------------------------------------------------------------------------
[theta11, theta12, theta21, theta22] = [2.5, 1, 4.5, 1]
[p1, p2, p3, p4, j1, j2, j3, j4] = [2, 0, 0, 1, 1, 0, 0.5, 0]
x0 = [3, 4]
num_sim = 248

randseed = np.random.randint(low=0, high=100000, size=(num_sim,))
n_real_log_price = n_bjd_simulation(
    random_seed=randseed,
    theta11=theta11, theta12=theta12, theta21=theta21, theta22=theta22,
    p1=p1, p2=p2, p3=p3, p4=p4, j1=j1, j2=j2, j3=j3, j4=j4,
    x0=x0, n_sim=num_sim)

n_real_price = log_price_to_price(n_log_price=n_real_log_price)
n_real_return = price_to_return(n_price=n_real_price)
n_real_stats = cal_stats(n_return=n_real_return, n_price=None)
# --------------------------------------------------------------------------------
params_vec = [(0.5, 0.5, 0.5, 0.5), (1, 1, 1, 1), (2, 2, 2, 2),
              (2.5, 4.5, 2, 1),
              (1.5, 4.5, 2, 1), (2, 4.5, 2, 1), (3, 4.5, 2, 1), (4, 4.5, 2, 1),
              (2.5, 3, 2, 1), (2.5, 4, 2, 1), (2.5, 5, 2, 1), (2.5, 6, 2, 1),
              (2.5, 4.5, 1, 1), (2.5, 4.5, 1.5, 1), (2.5, 4.5, 2.5, 1), (2.5, 4.5, 3, 1),
              (2.5, 4.5, 2, 0.5), (2.5, 4.5, 2, 1.5), (2.5, 4.5, 2, 2), (2.5, 4.5, 2, 4)
              ]
for i in params_vec:
    print(i, loss_function(i))
# --------------------------------------------------------------------------------

begin_time = datetime.datetime.now()
initial0 = [1, 1, 1, 1]
res = minimize(loss_function, initial0, method='Nelder-Mead', tol=1e-6, options={'disp': True})
print(datetime.datetime.now() - begin_time)
print(res.x)
# options={'disp': True, 'maxiter': 200}

# --------------------------------------------------------------------------------
begin_time2 = datetime.datetime.now()
res2 = minimize(loss_function, initial0, method='Powell', tol=1e-6, options={'disp': True})
print(datetime.datetime.now() - begin_time2)
print(res2.x)

# --------------------------------------------------------------------------------
begin_time3 = datetime.datetime.now()
res3 = minimize(loss_function, initial0, method='BFGS', tol=1e-6, options={'disp': True})
print(datetime.datetime.now() - begin_time3)
print(res3.x)

# --------------------------------------------------------------------------------
begin_time4 = datetime.datetime.now()
res4 = minimize(loss_function, initial0, method='L-BFGS-B', tol=1e-6, options={'disp': True})
print(datetime.datetime.now() - begin_time4)
print(res4.x)