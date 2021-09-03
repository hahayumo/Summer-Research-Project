library(httr)
library(tidyquant)
library(zoo) ## for data processing
library(tidyverse)
library(forecast)
library(Quandl)
library(tseries)
library(rugarch)


dat <- tq_get("AAPL",
              from = "2010-01-01",
              to = "2019-12-30") %>%
  mutate(return = log(adjusted / lag(adjusted))) %>%
  filter(!is.na(return))
return <- dat$return


# price series  ------
ggplot(dat, aes(x = date, y = adjusted)) + 
  geom_line() + 
  labs(title = 'Apple adjusted price 
       1 Jan 2010 - 30 Dec 2019',
       x = "Year",
       y = "Adjusted price")  

# Return versus date ------
ggplot(dat, aes(x = date, y = 100*return)) +   geom_line() + 
  ylim(-15, 15) +
  labs(title = 'Apple (log) return (%)
       1 Jan 2010 - 30 Dec 2019',
       x = "Year",
       y = "Return (%)")  


# Abs Return versus date ------
ggplot(dat, aes(x = date, y = 100*abs(return))) + 
  geom_line() + 
  ylim(0, 15) +
  labs(title = 'Apple absolute (log) return (%)
       1 Jan 2010 - 30 Dec 2019',
       x = "Year",
       y = "Absolute return (%)")  
















# ------
ggplot(dat, aes(x = 100*return)) + 
  geom_histogram(aes(y = ..density..), bins = 40, color = 'lightblue', fill = "royalblue1") +
  xlim(-10, 10) +
  geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = 100*mean(dat$return), sd = 100*sd(dat$return))) +
  scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = 'Apple (log) return (%)
       1 Jan 2010 - 30 Dec 2019',
       x = "Return (%)",
       y = "Density")

# ------
ggplot(dat, aes(sample = scale(return))) +
  stat_qq(col = "royalblue1") +
  stat_qq_line() + 
  labs(title = 'Apple standardised return
       1 Jan 2010 - 30 Dec 2019',
       x = 'N(0,1) quantile',
       y = 'Sample quantile')

T    = length(dat$return)
T
rbar = 1/T*sum(dat$return)
rbar
s    = sd(dat$return)
s
b    = (1/T*sum((dat$return - rbar)^3)) / (1/T*sum((dat$return - rbar)^2))^(3/2)
b #Skewness
k    = (1/T*sum((dat$return - rbar)^4)) / (1/T*sum((dat$return - rbar)^2))^2
k #Kurtosis

skewness=function(return){
  (1/T*sum((return - mean(return))^3)) / (1/T*sum((return - mean(return))^2))^(3/2)
}
Kurt=function(return){
  (1/T*sum((return - mean(return))^4)) / (1/T*sum((return - mean(return))^2))^2
}


set.seed(9868)
genbootsample <- function(data){
  sample(data, length(data), replace=TRUE)}
bootsd <- function(data, T, nrep){
  sd(replicate(nrep, T(genbootsample(data))))}

sd_mean <- bootsd(100*return, mean, 10000)
sd_mean
sd_sd <-bootsd(100*return, sd, 10000)
sd_sd
sd_skew <- bootsd(100*return, skewness, 10000)
sd_skew
sd_kurt <-bootsd(100*return, Kurt, 10000)
sd_kurt






## SF2&3
conf.level <- 0.95
ciline <- qnorm((1 - conf.level)/2)/sqrt(length(return))

acf_return <- acf(dat$return, lag = 50, plot = FALSE)
data_acf_return <- with(acf_return, data.frame(lag, acf))

ggplot(data_acf_return, aes(x = lag, y = acf)) + 
  geom_bar(stat = "identity", position = "identity", fill = "royalblue1") +
  geom_line(aes(y = ciline), linetype = "dotted", col = "blue") +
  geom_line(aes(y = -ciline), linetype = "dotted", col = "blue") +
  labs(title = 'Apple (log) return
       1 Jan 2010 - 30 Dec 2019',
       x = "Lag",
       y = "Autocorrelation")



acf_absolute_return <- acf(abs(dat$return), lag = 50, plot = FALSE)
data_absolute_acf_return <- with(acf_absolute_return, data.frame(lag, acf))

ggplot(data_absolute_acf_return, aes(x = lag, y = acf)) + 
  geom_bar(stat = "identity", position = "identity", fill = "royalblue1") +
  geom_line(aes(y = ciline), linetype = "dotted", col = "blue") +
  geom_line(aes(y = -ciline), linetype = "dotted", col = "blue") +
  labs(title = 'Apple absolute (log) return
       1 Jan 2010 - 30 Dec 2019',
       x = "Lag",
       y = "Autocorrelation")





#---- ccf
dat2 <- tq_get("MSFT",
              from = "2010-01-01",
              to = "2019-12-30") %>%
  mutate(return = log(adjusted / lag(adjusted))) %>%
  filter(!is.na(return))
return2 <- dat2$return

conf.level <- 0.95
ciline <- qnorm((1 - conf.level)/2)/sqrt(length(return))

ccf_return <- ccf(dat$return, dat2$return, lag = 50, plot = FALSE)
data_ccf_return <- with(ccf_return, data.frame(lag, acf))

ggplot(data_ccf_return, aes(x = lag, y = acf)) + 
  geom_bar(stat = "identity", position = "identity", fill = "royalblue1") +
  geom_line(aes(y = ciline), linetype = "dotted", col = "blue") +
  geom_line(aes(y = -ciline), linetype = "dotted", col = "blue") +
  labs(title = 'Apple and Microsoft (log) return
       1 Jan 2010 - 30 Dec 2019',
       x = "Lag",
       y = "Cross-correlation")



ccf_absolute_return <- ccf(abs(dat$return), abs(dat2$return), lag = 50, plot = FALSE)
data_absolute_ccf_return <- with(ccf_absolute_return, data.frame(lag, acf))








a=1
































































## (FTS.4.2)
sre <- as.numeric(residuals(fit, standardize = TRUE))
data <- data.frame(dat$date, sre)
ggplot(dat, aes(x = date, y = sre)) + 
  geom_line() +
  labs(title = 'Standardised GARCH(1,1) residual
       1 Jan 2010 - 30 Dec 2019',
       x = "Time",
       y = "value") 


## (FTS.4.4) Empirical ACFs of the standardised residuals of the GARCH(1,1) process and their absolute values
conf.level <- 0.95
ciline <- qnorm((1 - conf.level)/2)/sqrt(length(sre))

acf_return <- acf(sre, lag = 50, plot = FALSE)
data_acf_return <- with(acf_return, data.frame(lag, acf))

ggplot(data_acf_return, aes(x = lag, y = acf)) + 
  geom_bar(stat = "identity", position = "identity", fill = "royalblue1") +
  geom_line(aes(y = ciline), linetype = "dotted", col = "blue") +
  geom_line(aes(y = -ciline), linetype = "dotted", col = "blue") +
  labs(title = 'Standardised GARCH(1,1) residual
       1 Jan 2010 - 30 Dec 2019',
       x = "Lag",
       y = "Autocorrelation")

acf_absolute_return <- acf(abs(sre), lag = 50, plot = FALSE)
data_absolute_acf_return <- with(acf_absolute_return, data.frame(lag, acf))

ggplot(data_absolute_acf_return, aes(x = lag, y = acf)) + 
  geom_bar(stat = "identity", position = "identity", fill = "royalblue1") +
  geom_line(aes(y = ciline), linetype = "dotted", col = "blue") +
  geom_line(aes(y = -ciline), linetype = "dotted", col = "blue") +
  labs(title = 'Absolute value of standardised GARCH(1,1) residual
       1 Jan 2010 - 30 Dec 2019',
       x = "Lag",
       y = "Autocorrelation")






