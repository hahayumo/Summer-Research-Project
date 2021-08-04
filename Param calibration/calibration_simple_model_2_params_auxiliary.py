
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

def one_sim(T=1, n=100, X0=100, mu=0, sigma=1):

    t = np.linspace(0, T, n+1)
    X = [X0]

    random.seed(123)
    for i in range(n):
        X_new = X[i] + mu*(t[i+1]-t[i]) + sigma*np.random.normal(0, t[i+1]-t[i], 1)
        X.append(float(X_new))
    return X

y = one_sim(T=1, n=100, X0=100, mu=0, sigma=1)
x = np.linspace(0, 1, 101)
plt.plot(x, y, 'r-')
plt.show()

#####
def create_simulation_data(T=1, n=100, X0=100, mu=0, sigma=1):

    data = []
    for i in range(n):
        new_data = one_sim(T=T, n=n, X0=X0, mu=0, sigma=1)
        data.append(new_data)

    data = pd.DataFrame(data).transpose()
    return data

T = 10
n = 200
X0 = 100
mu = 2
sigma = 3
sim_data = create_simulation_data(T=T, n=n, X0=X0, mu=mu, sigma=sigma)

def create_stats(sim_data):

    mean = sim_data.mean(axis=0)
    sd = sim_data.std(axis=0)
    stats_data = pd.DataFrame([mean, sd]).transpose()
    return stats_data
stats_data = create_stats(sim_data)

####
def loss_function(params):

    mu = params[0]
    sigma = params[1]
    penalty_mean = []
    penalty_sd = []
    for i in range(stats_data.shape[0]):
        one_sim = one_sim(T=T, n=n, X0=X0, mu=mu, sigma=sigma)
        mean = np.mean(one_sim)
        sd = np.std(one_sim)
        penalty_mean.append((mean - stats_data.iloc[i, 0])**2)
        penalty_sd.append((sd - stats_data.iloc[i, 1])**2)

    #standardised_penalty_mean = penalty_mean / np.max(penalty_mean)
    #standardised_penalty_sd = penalty_sd / np.max(penalty_sd)
    #standardised_penalty_mean = np.log(penalty_mean)
    #standardised_penalty_sd = np.log(penalty_sd)
    standardised_penalty_mean = penalty_mean
    standardised_penalty_sd = penalty_sd

    value1 = sum(standardised_penalty_mean)
    value2 = sum(standardised_penalty_sd)
    return value1 + value2

params_vec = [(0,0.5),(0,0.75),(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(2,3),(2,4),(3,4)]
for i in params_vec:
    print(i, loss_function(i))

######################################################################

x0 = [1, 1]
res = minimize(loss_function, x0, method='L-BFGS-B', tol=1e-6, options={'disp': True})
res.x












