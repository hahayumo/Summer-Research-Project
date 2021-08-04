
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
from scipy.optimize import basinhopping
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
    stats_data = pd.DataFrame([mean, sd]).transpose()
    return stats_data





def loss_function(params):

    mu = params[0]
    sigma = params[1]
    moment_loss = pd.DataFrame().reindex_like(real_stats)

    n_sim_data = np.exp(n_sim(T=T, n=n, X0=X0, mu=mu, sigma=sigma))
    n_sim_return = price_to_return(n_sim_data)
    sim_stats = cal_stats(n_sim_return)

    for i in range(real_stats.shape[0]):
        moment_loss.iloc[i, 0] = np.sqrt((real_stats.iloc[i, 0] - sim_stats.iloc[i, 0])**2)
        moment_loss.iloc[i, 1] = np.sqrt((real_stats.iloc[i, 1] - sim_stats.iloc[i, 1])**2)

    #for m in range(moments.shape[1]):
        #moment_loss.iloc[:, m] = np.log(moment_loss.iloc[:, m])

    sum_all = np.sum(moment_loss)
    moments1 = sum_all[0] #/ np.max(moment_loss.iloc[:, 0])
    moments2 = sum_all[1] #/ np.max(moment_loss.iloc[:, 1])
    return moments1 + moments2






T = 1
n = 200
X0 = 3

mu = 0.5
sigma = 2

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


begin_time = datetime.datetime.now()
x0 = [1, 1]

# res = minimize(loss_function, x0, method='Nelder-Mead', tol=1e-6, options={'disp': True})
# Warning: Maximum number of function evaluations has been exceeded.
# 0:02:58.942100
# [0.95019989 1.08250503]

# res = minimize(loss_function, x0, method='Nelder-Mead', tol=1e-4, options={'disp': True})
# Warning: Maximum number of function evaluations has been exceeded.
# 0:02:57.709026
# [0.33616197 1.87039902]

res = basinhopping(func=loss_function, x0=x0, niter=200, minimizer_kwargs={"method": "BFGS"})


# res = minimize(loss_function, x0, method='Powell', tol=1e-4, options={'disp': True})
# Optimization terminated successfully.
#          Current function value: 100.318871
#          Iterations: 3
#          Function evaluations: 100
# 0:00:44.222273
# [0.66300821 2.01301089]

# res = minimize(loss_function, x0, method='Powell', tol=1e-6, options={'disp': True})
# Optimization terminated successfully.
#          Current function value: 94.969001
#          Iterations: 2
#          Function evaluations: 102
# 0:00:44.958575
# [0.3728467  2.06394234]

print(datetime.datetime.now() - begin_time)
print(res.x)


