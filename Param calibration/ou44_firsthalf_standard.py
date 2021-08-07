#!/usr/bin/python3
#PBS -N ou44firsthalf_standard
#PBS -m bea
#PBS -q standard

# Obtain 4 true values of parameters for the Ornstein-Uhlenbeck process by calibrating the model to the real market pair stocks from S&P 500

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



# Define the model that generates pair simulations.
np.random.seed(9868)
yuima = importr("yuima")
n_ou_sim_string = """
n_sim_ou = function(random_seed, num_sim,
                    mu11, mu12, mu21, mu22, sigma11, sigma12, sigma21, sigma22,
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



# Define some function that transforms price to return or the reverse.
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



# Define the function of transforming returns data into feature statistics (or moments).
def cal_stats(n_return, n_price=None):
    # (different expressions of calculation from intro to stat finance)
    # 4 statistics
    return_series1 = n_return.iloc[:, ::2]
    return_series2 = n_return.iloc[:, 1::2]
    mean1 = return_series1.mean(axis=0).values
    sd1 = return_series1.std(axis=0).values
    mean2 = return_series2.mean(axis=0).values
    sd2 = return_series2.std(axis=0).values
    stats_data = pd.DataFrame([mean1, mean2, sd1, sd2])
    stats_data = stats_data.transpose()
    stats_data.columns = [
        'return_mean1', 'return_mean2',
        'return_sd1', 'return_sd2']
    return stats_data



# Define the loss function as the sum of the absolute differences between moments of real market return data and simulated return data
def loss_function(params):
    """n_real_stats is a global amount calculated outside the function"""
    params = FloatVector(params)
    moment_loss = pd.DataFrame().reindex_like(n_real_stats)
    randseed = np.random.randint(low=0, high=1000000, size=(1,))
    n_sim_log_price = n_ou_simulation(
        random_seed=int(randseed), num_sim=num_sim,
        mu11=mu11, mu12=params[0], mu21=mu21, mu22=params[1],
        sigma11=params[2], sigma12=sigma12, sigma21=sigma21, sigma22=params[3],
        xinit=xinit, T0=T0, T=T, length=length)
    n_sim_price = log_price_to_price(n_sim_log_price)
    n_sim_return = price_to_return(n_sim_price)
    n_sim_stats = cal_stats(n_sim_return)
    for i in range(n_real_stats.shape[0]):
        for j in range(n_real_stats.shape[1]):
            moment_loss.iloc[i, j] = np.sqrt((n_real_stats.iloc[i, j] - n_sim_stats.iloc[i, j])**2)
    sum_all = np.sum(moment_loss)
    return np.sum(sum_all)



# Import the real market pair return data and prepare the corresponding initial log-prices of pair stocks for the following simulation and optimisation work.
# 4 params are: mu12, mu22, sigma11, sigma22

n_real_price = pd.read_csv("real_pair_prices.csv", index_col=[0])
n_real_log_price = price_to_log_price(n_real_price)

n_real_return = pd.read_csv("real_pair_returns.csv", index_col=[0])
n_real_stats = cal_stats(n_return=n_real_return, n_price=None)

# fixed constants are:
mu11, mu21, sigma12, sigma21 = 0, 0, -1000, -1000

xinit = [4, 5]

num_sim, T0, T, length = n_real_stats.shape[0], 0, 1, n_real_price.shape[0]
# num_sim 248 and length 250



# The calibration process can be seen as a process of seeking for a set of values of the parameters such that the simulations are the closest to the real data in a sense that the feature statistics of simulations are matched with those of real returns such that the total losses are minimised. Also, we will see the losses of moments.

np.random.seed(9868)

initial0 = [1, 1, 1, 1]

# Look at the optimisation results
begin_time = datetime.datetime.now()
res = minimize(loss_function, initial0, method='Powell',
               tol=1e-6, options={'disp': True})
print(res.x)

# Look at the running time
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
    mu11=mu11, mu12=params[0], mu21=mu21, mu22=params[1],
    sigma11=params[2], sigma12=sigma12, sigma21=sigma21, sigma22=params[3],
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
# n_sim_price.to_csv("ou_4params_price.csv")
# n_sim_return.to_csv("ou_4params_return.csv")
