import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
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
import datetime
np.random.seed(123)

def one_sim(T=1, n=100, X0=3, mu=0, sigma=1):

    t = np.linspace(0, T, n+1)
    X = [X0]

    for i in range(n):
        X_new = X[i] + mu*(t[i+1]-t[i]) + sigma*np.random.normal(0, t[i+1]-t[i], 1)
        X.append(float(X_new))
    return X
def n_sim(T=1, n=100, X0=3, mu=0, sigma=1):

    data = []
    for i in range(n):
        new_data = one_sim(T=T, n=n, X0=X0, mu=mu, sigma=sigma)
        data.append(new_data)

    data = pd.DataFrame(data).transpose()
    return data
def price_to_return(n_price):

    n_real_return = pd.DataFrame()
    for i in range(n_price.shape[1]):
        ith_column_price_series = n_price.iloc[:, i]
        n_real_return = pd.concat([n_real_return, 100 * np.log(ith_column_price_series[1:].values / ith_column_price_series[:-1])], axis=1)
    return n_real_return
def cal_stats(n_data):

    mean = n_data.mean(axis=0).values
    sd = n_data.std(axis=0).values
    skew = n_data.skew(axis=0).values
    kurtosis = n_data.kurtosis(axis=0).values
    stats_data = pd.DataFrame([mean, sd, skew, kurtosis]).transpose()
    stats_data.columns = ['return_mean', 'return_sd', 'return_skew', 'return_kurtosis']
    return stats_data
def loss_function(params):

    mu = params[0]
    sigma = params[1]
    moment_loss = pd.DataFrame().reindex_like(real_stats)

    n_sim_data = np.exp(n_sim(T=T, n=n, X0=X0, mu=mu, sigma=sigma))
    n_sim_return = price_to_return(n_sim_data)
    sim_stats = cal_stats(n_sim_return)

    for i in range(real_stats.shape[0]):
        for j in range(real_stats.shape[1]):
            moment_loss.iloc[i, j] = np.sqrt((real_stats.iloc[i, j] - sim_stats.iloc[i, j])**2)

    sum_all = np.sum(moment_loss)
    return np.sum(sum_all)

T, n, X0 = 1, 200, 3

mu, sigma = 0.5, 2

n_real_data = np.exp(n_sim(T=T, n=n, X0=X0, mu=mu, sigma=sigma))
n_real_return = price_to_return(n_real_data)
real_stats = cal_stats(n_real_return)

params_vec = [(0, 0.5), (0, 0.75), (0, 1), (0, 2), (0, 3), (0, 4),
              (0.2, 3), (0.4, 3),
              (0.5, 1), (0.5, 2), (0.5, 3), (0.5, 5), (0.5, 6),
              (0.6, 10),
              (1, 1), (1, 2), (1, 3),
              (2, 1), (2, 2), (2, 3), (2, 4),
              (3, 4)]
for i in params_vec:
    print(i, loss_function(i))

"""-----------------------------------------------------------------"""
begin_time = datetime.datetime.now()
x0 = [1, 1]
res = minimize(loss_function, x0, method='Nelder-Mead', tol=1e-6, options={'disp': True})
print(datetime.datetime.now() - begin_time)
print(res.x)
"""-----------------------------------------------------------------"""
begin_time2 = datetime.datetime.now()
res2 = minimize(loss_function, x0, method='Powell', tol=1e-6, options={'disp': True})
print(datetime.datetime.now() - begin_time2)
print(res2.x)