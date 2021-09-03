library(httr)
library(tidyquant)
library(zoo) ## for data processing
library(tidyverse)
library(forecast)
library(Quandl)
library(tseries)
library(rugarch)

dat = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_returns_cal.csv', row.names = 1)
dat1 = dat[, seq(1,496,2)]
dat1 = data.frame(unlist(dat1))
colnames(dat1) = 'return1'
dat2 = dat[, seq(2,496,2)]
dat2 = data.frame(unlist(dat2))
colnames(dat2) = 'return2'

return1 = dat1$return1
return2 = dat2$return2



# ------
ggplot(dat1, aes(x = return1)) + 
  geom_histogram(aes(y = ..density..), bins = 80, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat1$return1), sd = sd(dat1$return1))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(Calibration use) 1st return series of 248 pairs
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")




# ------
ggplot(dat2, aes(x = return2)) + 
  geom_histogram(aes(y = ..density..), bins = 80, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat2$return2), sd = sd(dat2$return2))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(Calibration use) 2nd return series of 248 pairs
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")

##############################################################################
##############################################################################
##############################################################################
##############################################################################

dat = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_returns_classify.csv', row.names = 1)
dat1 = dat[, seq(1,496,2)]
dat1 = data.frame(unlist(dat1))
colnames(dat1) = 'return1'
dat2 = dat[, seq(2,496,2)]
dat2 = data.frame(unlist(dat2))
colnames(dat2) = 'return2'

return1 = dat1$return1
return2 = dat2$return2



# ------
ggplot(dat1, aes(x = return1)) + 
  geom_histogram(aes(y = ..density..), bins = 80, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat1$return1), sd = sd(dat1$return1))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(Classification use) 1st return series of 248 pairs
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")



ggplot(dat2, aes(x = return2)) + 
  geom_histogram(aes(y = ..density..), bins = 80, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat2$return2), sd = sd(dat2$return2))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(Classification use) 2nd return series of 248 pairs
       1 Jan 2000 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")