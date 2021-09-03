library(tidyquant)
library(tidyverse) 
library(testthat)
start_date = "2020-01-01"
end_date = "2021-12-31"

stock = tq_index("SP500")
stock_symbols = stock$symbol
dates = tq_get("AAPL", from=start_date, to=end_date)$date
num_dates = length(dates)

# extract the historical adjusted closing price data
one_stock_price = function(stock_symbol, start_date, end_date){
  tq_get(stock_symbol, from = start_date, to = end_date) %>% filter(!is.na(adjusted))}
# download all the stock prices during the time period
stock_prices = sapply(1:length(stock_symbols), function(i){return(tryCatch(one_stock_price(stock_symbols[i], start_date, end_date)$adjusted, error=function(e) NULL))})
warnings = warnings()




library(stringi)
real_stock_prices <- data.frame(t(as.data.frame(stri_list2matrix(stock_prices, byrow = TRUE), stringsAsFactors=FALSE)))

a = Filter(function(x) !(all(x=="")), real_stock_prices)
a = Filter(function(x) !(all(x=="NA")), a)
real_stock_prices = Filter(function(x) !(all(x=="NULL")), a)
for (i in 1:dim(real_stock_prices)[2]){
  real_stock_prices[, i] = as.numeric(real_stock_prices[, i])
}
  
lens = c()
for (i in 1:length(stock_prices)){
  lens = c(lens, length(stock_prices[[i]]))}


real_stock_returns = data.frame(
  sapply(1:dim(real_stock_prices)[2], 
         function(i){
           100 * (log(real_stock_prices[,i][-1]) - log(real_stock_prices[,i][-dim(real_stock_prices)[1]]))}))




price_20_21 = real_stock_prices
return20_21 = real_stock_returns
return20_21 = data.frame(unlist(return20_21))
colnames(return20_21) = 'return1'
dat1 = return20_21

ggplot(dat1, aes(x = return1)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) + ylim(0, 0.35) +
  #geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  #stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat1$return1), sd = sd(dat1$return1))) +
  #scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(log) return of 496 stocks 
       1 Jan 2020 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")


dat2 = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_20180101_20191231/sp500_20180101_20191231_pair_returns.csv', row.names = 1)
dat2 = data.frame(unlist(dat2))
colnames(dat2) = 'return2'

# ------
ggplot(dat2, aes(x = return2)) + 
  geom_histogram(aes(y = ..density..), bins = 60, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) + ylim(0,0.35) +
  #geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  #stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat2$return2), sd = sd(dat2$return2))) +
  #scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(log) return of 496 stocks
       1 Jan 2018 - 31 Dec 2019',
       x = "Return (%)",
       y = "Density")


dat3 = dat2[1:(dim(dat2)[1]/2), ]
dat3 = data.frame(dat3)
colnames(dat3) = 'return2'
# ------
ggplot(dat3, aes(x = return2)) + 
  geom_histogram(aes(y = ..density..), bins = 80, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) + ylim(0,0.35) +
  #geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  #stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat2$return2), sd = sd(dat2$return2))) +
  #scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(log) return of first 248 stocks
       1 Jan 2018 - 31 Dec 2019',
       x = "Return (%)",
       y = "Density")



dat4 = dat2[(dim(dat2)[1]/2):(dim(dat2)[1]), ]
dat4 = data.frame(dat4)
colnames(dat4) = 'return2'
# ------
ggplot(dat4, aes(x = return2)) + 
  geom_histogram(aes(y = ..density..), bins = 80, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) + ylim(0,0.35) +
  #geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  #stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat2$return2), sd = sd(dat2$return2))) +
  #scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(log) return of last 248 stocks
       1 Jan 2018 - 31 Dec 2019',
       x = "Return (%)",
       y = "Density")























dat3 = dat1[1:(dim(dat1)[1]/2), ]
dat3 = data.frame(dat3)
colnames(dat3) = 'return2'
# ------
ggplot(dat3, aes(x = return2)) + 
  geom_histogram(aes(y = ..density..), bins = 80, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) + ylim(0,0.35) +
  #geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  #stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat2$return2), sd = sd(dat2$return2))) +
  #scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(log) return of first 248 stocks
       1 Jan 2020 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")



dat4 = dat1[(dim(dat1)[1]/2):(dim(dat1)[1]), ]
dat4 = data.frame(dat4)
colnames(dat4) = 'return2'
# ------
ggplot(dat4, aes(x = return2)) + 
  geom_histogram(aes(y = ..density..), bins = 80, color = 'lightblue', fill = "royalblue1") +
  xlim(-15, 15) + ylim(0,0.35) +
  #geom_density(aes(colour = "Kernel"), adjust = 1, alpha = 1) +
  #stat_function(aes(colour = "Normal"), fun = dnorm, args = list(mean = mean(dat2$return2), sd = sd(dat2$return2))) +
  #scale_colour_manual(name = '', values = c('blue', 'red')) +
  labs(title = '(log) return of last 248 stocks
       1 Jan 2020 - 1 Aug 2021',
       x = "Return (%)",
       y = "Density")
