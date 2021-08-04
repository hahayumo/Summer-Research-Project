
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
import rpy2

from rpy2.robjects.packages import importr
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
yuima = importr("yuima")
one_bjd_sim_string = """
one_sim_jump_diff = function(theta11 = 10, theta12 = 1, theta21 = 10, theta22=1, 
                             p1 = 2, p2 = 0.5, p3 = 1, p4 = 1, 
                             j1 = 1, j2 =   2, j3 = 4, j4 = 1,
                             x0 = c(2, 3)){
  
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


# one simulation of bivariate jump diffusion model
def one_bjd_simulation(theta11=10, theta12=1, theta21=10, theta22=1,
                       p1=2, p2=0.5, p3=1, p4=1,
                       j1=1, j2=2, j3=4, j4=1,
                       x0=[4, 5]):

    one_bjd_sim_data = pd.DataFrame(
        one_bjd_sim.one_sim_jump_diff(
            theta11=theta11, theta12=theta12, theta21=theta21, theta22=theta22,
            p1=p1, p2=p2, p3=p3, p4=p4,
            j1=j1, j2=j2, j3=j3, j4=j4,
            x0=x0)).transpose()
    return one_bjd_sim_data

one_bjd_simulation()




























