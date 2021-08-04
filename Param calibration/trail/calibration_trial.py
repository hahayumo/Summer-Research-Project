
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

def bm(T=1, n=100, W0=100):

    t = np.linspace(0, T, n+1)
    W = [W0]

    random.seed(123)
    for i in range(n):
        W_new = W[i] + np.sqrt(t[i+1]-t[i]) * np.random.normal(0, 1, 1)
        W.append(float(W_new))
    return W

y = bm(T=1, n=100, W0=0)
x = np.linspace(0, 1, 101)

plt.plot(x, y, 'r-')
plt.title("Brownian Motion")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

######################################################################
def gbm(mu, sigma, T=1, n=100, S0=100):

    t = np.linspace(0, T, n+1)
    S = S0 * np.exp((mu-sigma**2)*t + sigma*np.array(bm(T=T, n=n, W0=0)))
    return S

y2 = gbm(mu=0, sigma=1, T=1, n=100, S0=100)
plt.plot(x, y2, 'b-')
plt.title("Geometric Brownian Motion")
plt.xlabel("x")
plt.ylabel("y2")
plt.show()

######################################################################
######################################################################

def create_simulation_data(num_sim=100, mu=0, sigma=1):

    data = []
    for i in range(num_sim):
        new_data = gbm(T=1, n=200, S0=100, mu=mu, sigma=sigma)
        data.append(new_data)

    data = pd.DataFrame(data).transpose()
    return data
num_sim = 500
sim_data = create_simulation_data(num_sim=num_sim, mu=0, sigma=1)

def create_stats(sim_data):

    mean = sim_data.mean(axis=0)
    sd = sim_data.std(axis=0)
    stats_data = pd.DataFrame([mean, sd]).transpose()
    return stats_data
stats_data = create_stats(sim_data)

######################################################################

def loss_function(mu, sigma):

    penalty_mean = []
    penalty_sd = []
    for i in range(stats_data.shape[0]):
        one_sim = gbm(mu=mu, sigma=sigma, T=1, n=200, S0=100)
        mean = np.mean(one_sim)
        sd = np.std(one_sim)
        penalty_mean.append((mean - stats_data.iloc[i, 0])**2)
        penalty_sd.append((sd - stats_data.iloc[i, 1])**2)

    standardised_penalty_mean = (penalty_mean - np.mean(penalty_mean)) / np.std(penalty_mean)
    standardised_penalty_sd = (penalty_sd - np.mean(penalty_sd)) / np.std(penalty_sd)
    value1 = sum(standardised_penalty_mean)
    value2 = sum(standardised_penalty_sd)
    return value1 + value2


z1 = loss_function(0, 1)
z2 = loss_function(0, 2)
z3 = loss_function(0, 3)
z4 = loss_function(0, 4)
z5 = loss_function(1, 2)
z6 = loss_function(2, 3)
z7 = loss_function(3, 4)

















