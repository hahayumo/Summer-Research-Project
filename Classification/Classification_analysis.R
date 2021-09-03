library(httr)
library(tidyquant)
library(zoo) ## for data processing
library(tidyverse)
library(forecast)
library(Quandl)
library(tseries)
library(rugarch)

return_real = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp600_mixed_period_2000_2021/pair_returns_classify.csv', row.names = 1)
return_ou = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/cal_ou/n_sim_ou_pair_returns.csv', row.names = 1)
return_jumpou = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/cal_jumpou/n_sim_jumpou_pair_returns.csv', row.names = 1)
return_stvol = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/cal_stvol/n_sim_stvol_pair_returns.csv', row.names = 1)

real_ts_1 = return_real[, seq(1,496,2)]
real_ts_2 = return_real[, seq(2,496,2)]
ou_ts_1 = return_ou[, seq(1,496,2)]
ou_ts_2 = return_ou[, seq(2,496,2)]
jumpou_ts_1 = return_jumpou[, seq(1,496,2)]
jumpou_ts_2 = return_jumpou[, seq(2,496,2)]
stvol_ts_1 = return_stvol[, seq(1,496,2)]
stvol_ts_2 = return_stvol[, seq(2,496,2)]

real_ts_1 = data.frame(unlist(real_ts_1))
real_ts_2 = data.frame(unlist(real_ts_2))
ou_ts_1 = data.frame(unlist(ou_ts_1))
ou_ts_2 = data.frame(unlist(ou_ts_2))
jumpou_ts_1 = data.frame(unlist(jumpou_ts_1))
jumpou_ts_2 = data.frame(unlist(jumpou_ts_2))
stvol_ts_1 = data.frame(unlist(stvol_ts_1))
stvol_ts_2 = data.frame(unlist(stvol_ts_2))

colnames(real_ts_1) = 'return'
colnames(real_ts_2) = 'return'
colnames(ou_ts_1) = 'return'
colnames(ou_ts_2) = 'return'
colnames(jumpou_ts_1) = 'return'
colnames(jumpou_ts_2) = 'return'
colnames(stvol_ts_1) = 'return'
colnames(stvol_ts_2) = 'return'

###########################################################################
dat = real_ts_1
ggplot(dat, aes(x = return)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) + ylim(0, 0.45) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm,
                args = list(mean = mean(dat$return), sd = sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(real-market return of first series)
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")

dat = real_ts_2
ggplot(dat, aes(x = return)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) + ylim(0, 0.45) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm,
                args = list(mean = mean(dat$return), sd = sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(real-market return of second series)
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")

###########################################################################
dat = ou_ts_1
ggplot(dat, aes(x = return)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) + ylim(0, 0.45) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm,
                args = list(mean = mean(dat$return), sd = sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(O-U simulated return of first series)
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")

dat = ou_ts_2
ggplot(dat, aes(x = return)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) + ylim(0, 0.45) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm,
                args = list(mean = mean(dat$return), sd = sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(O-U simulated return of second series)
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")

###########################################################################
dat = jumpou_ts_1
ggplot(dat, aes(x = return)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) + ylim(0, 0.45) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm,
                args = list(mean = mean(dat$return), sd = sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(jump O-U simulated return of first series)
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")

dat = jumpou_ts_2
ggplot(dat, aes(x = return)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) + ylim(0, 0.45) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm,
                args = list(mean = mean(dat$return), sd = sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(jump O-U simulated return of second series)
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")

###########################################################################
dat = stvol_ts_1
ggplot(dat, aes(x = return)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) + ylim(0, 0.45) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm,
                args = list(mean = mean(dat$return), sd = sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(stochastic volatility simulated return of first series)
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")


dat = stvol_ts_2
ggplot(dat, aes(x = return)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) + ylim(0, 0.45) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm,
                args = list(mean = mean(dat$return), sd = sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(stochastic volatility simulated return of second series)
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")










###########################################################################
# Prediction of accuracy plot
acc_ou = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/cal_ou/results_ou.csv', row.names = 1)
acc_jumpou = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/cal_jumpou/results_oujump.csv', row.names = 1)
acc_stvol = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/cal_stvol/results_stvol.csv', row.names = 1)
acc_ou = data.frame(acc_ou[1:30,])

acc_ou_val = cumsum(acc_ou) / seq(1,30,1)
acc_jumpou_val = cumsum(acc_jumpou) / seq(1,30,1)
acc_stvol_val = cumsum(acc_stvol) / seq(1,30,1)

par(mfrow=c(1, 1))

data = data.frame(acc_ou_val, acc_jumpou_val, acc_stvol_val)
data = 1-data
ggplot(data, aes(seq(1, 30, 1))) + 
  geom_line(aes(y=acc_ou.1.30..., colour="O-U")) +
  geom_line(aes(y=X0, colour='O-U with NIG jump')) +
  geom_line(aes(y=X0.1, colour='Stochastic volatility')) + 
  ylim(0, 0.1) +
  labs(x = "Iteration",
       y = "Error rate")


print(mean(acc_ou$X0))
print(mean(acc_jumpou$X0))
print(mean(acc_stvol$X0))
print(sd(acc_ou$X0))
print(sd(acc_jumpou$X0))
print(sd(acc_stvol$X0))









################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
clean_data = read.csv("/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/cal_ou/clean_data.csv", row.names = 1)
loss = clean_data$loss

# losses
ggplot(clean_data, aes(x = seq(1,length(loss),1), y = loss)) + 
  geom_point() + 
  labs(title = 'Calibration loss of the final iteration
       O-U model',
       x = "Iteration",
       y = "Loss") +
  ylim(1460, 1600)

# 







a= read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/cal_stvol/clean_data.csv', row.names = 1)
mean(a$time)

