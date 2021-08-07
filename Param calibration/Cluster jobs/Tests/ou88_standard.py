#!/usr/bin/python3
#PBS -N ou88_standard
#PBS -m bea
#PBS -q standard

import pandas as pd
import numpy as np
import random
from numpy.random import RandomState
from scipy import stats
from scipy.optimize import minimize
import os
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
  diffusion = matrix(c("exp(sigma11)", "exp(sigma12)", "exp(sigma21)", "exp(sigma22)"), 2, 2, byrow=TRUE)
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
    """num_sim simulations of bivariate Ornstein-Uhlenbeck process,
    length = length of one series
    """
    n_ou_sim_data = pd.DataFrame(
        n_ou_sim.n_sim_ou(random_seed=random_seed, num_sim=num_sim,
                          mu11=mu11, mu12=mu12, mu21=mu21, mu22=mu22,
                          sigma11=sigma11, sigma12=sigma12, sigma21=sigma21, sigma22=sigma22,
                          xinit=xinit, T0=T0, T=T, length=length)).transpose()
    return n_ou_sim_data

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
    """ 8 statistics
    'skewness' and 'kurtosis' are of different expressions from the course of 'intro to stat finance') """
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
    return np.sum(sum_all)


# 8 params are mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22

n_real_price = pd.read_csv("real_pair_prices.csv", index_col=[0])
n_real_log_price = price_to_log_price(n_real_price)

n_real_return = pd.read_csv("real_pair_returns.csv", index_col=[0])
n_real_stats = cal_stats(n_return=n_real_return, n_price=None)


# fixed constants are:
xinit = [4, 5]

num_sim, T0, T, length = n_real_stats.shape[0], 0, 1, n_real_price.shape[0]
# num_sim 248 and length 250

np.random.seed(9868)

initial0 = [1, 1, 1, 1, 1, 1, 1, 1]

# Look at the optimisation results
begin_time = datetime.datetime.now()
res = minimize(loss_function, initial0, method='Powell',
               tol=1e-6, options={'disp': True})
print(res.x)

#  Look at the running time
time = datetime.datetime.now() - begin_time
print(time)

# Look at the scales of losses of different moments
np.random.seed(9868)
params = (res.x)
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

for k in range(n_real_stats.shape[0]):
    for j in range(n_real_stats.shape[1]):
        moment_loss.iloc[k, j] = np.sqrt((n_real_stats.iloc[k, j] -
                                          n_sim_stats.iloc[k, j]) ** 2)

sum_all = np.sum(moment_loss)
print(sum_all)


































random_seed = 9868

mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22 = params

num_sim, T0, T, length = 248, 0, 1, 250
np.random.seed(9868)
n_real_log_price = n_ou_simulation(
    random_seed=random_seed, num_sim=num_sim,
    mu11=mu11, mu12=mu12, mu21=mu21, mu22=mu22,
    sigma11=sigma11, sigma12=sigma12, sigma21=sigma21, sigma22=sigma22,
    xinit=xinit, T0=T0, T=T, length=length)
n_real_price = log_price_to_price(n_log_price=n_real_log_price)
n_real_return = price_to_return(n_price=n_real_price)
n_real_stats = cal_stats(n_return=n_real_return, n_price=None)

np.random.seed(9868)

params_vec = [(mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22),
              (mu11-1, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22),
              (mu11+1, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22),
              (mu11, mu12-1, mu21, mu22, sigma11, sigma12, sigma21, sigma22),
              (mu11, mu12+1, mu21, mu22, sigma11, sigma12, sigma21, sigma22),
              (mu11, mu12, mu21-1, mu22, sigma11, sigma12, sigma21, sigma22),
              (mu11, mu12, mu21+1, mu22, sigma11, sigma12, sigma21, sigma22),
              (mu11, mu12, mu21, mu22-1, sigma11, sigma12, sigma21, sigma22),
              (mu11, mu12, mu21, mu22+1, sigma11, sigma12, sigma21, sigma22),
              (mu11, mu12, mu21, mu22, sigma11-1, sigma12, sigma21, sigma22),
              (mu11, mu12, mu21, mu22, sigma11+1, sigma12, sigma21, sigma22),
              (mu11, mu12, mu21, mu22, sigma11, sigma12-1, sigma21, sigma22),
              (mu11, mu12, mu21, mu22, sigma11, sigma12+1, sigma21, sigma22),
              (mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21-1, sigma22),
              (mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21+1, sigma22),
              (mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22-1),
              (mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22+1)]
for i in params_vec:
    print(i, loss_function(i))




np.random.seed(9868)
initial0 = [1, 1, 1, 1, 1, 1, 1, 1]
results = []

for num_iter in range(5):

    # look at the ith iteration
    print(num_iter)

    begin_time = datetime.datetime.now()
    print(begin_time)

    # look at the results of the optimisation
    res = minimize(loss_function, initial0, method='Powell', tol=1e-6, options={'disp': True})
    print(res.x)

    # look at the time consumed
    time = datetime.datetime.now() - begin_time
    print(time)

    #  look at the losses of moments
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
            moment_loss.iloc[i, j] = np.sqrt((n_real_stats.iloc[i, j] - n_sim_stats.iloc[i, j]) ** 2)

    sum_all = np.sum(moment_loss)
    print(sum_all)

    results.append([res.x, time, sum_all])


results_res = []
results_time = []
results_sum_all = []
for i in results:
    results_res.append(i[0])
    results_time.append(i[1])
    results_sum_all.append(i[2])

res_mean = pd.DataFrame(results_res).mean(axis=0)
res_std  = pd.DataFrame(results_res).std(axis=0)
print(res_mean)
print(res_std)
