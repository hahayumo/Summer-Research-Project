# This file presents how to obtain the historical adjusted closing prices of each stock in S&P 500 during  'start_date' and 'end_date' using R package "tidyquant".
# You can set 'start_date' and 'end_date' as any available historical date that are of your interest and set the "folder_path" as where you download the project folder. The following "folder_path" is where the author saves the data file in a personal computer.

start_date = "2018-01-01"
end_date = "2018-12-31"
folder_path = "/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub"

library(tidyquant)
library(tidyverse) 
library(testthat)
data_path = "/Summer-Research-Project/Data/"
date_path = paste('sp500', gsub('-','',start_date), gsub('-','',end_date), sep='_')

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

lens = c()
for (i in 1:length(stock_prices)){
  lens = c(lens, length(stock_prices[[i]]))}
print(sum(lens==0))
print(sum(lens==250))
# Locate the stocks with less than 250 observation prices during the period
print(which(lens!=250 & lens!=0)) 
print(stock_symbols[which(lens!=250 & lens!=0)]) 



# According to warnings and length of observations
real_stock_symbols = stock_symbols[-c(match(c("BRK.B","MRNA","DOW","CARR","OTIS","CTVA","BF.B","FOXA","OGN","FOX", "VSCO"), stock_symbols))]
# remove "MRNA" since it contains only 15 observations in 2018, instead we replace it with "ALXN" according to the latest replacement updated in the Wikipedia
real_stock_symbols = c(real_stock_symbols, "ALXN")
# download all the stock prices during the time period again using the new real_stock_symbols
stock_prices = sapply(1:length(real_stock_symbols), function(i){return(tryCatch(one_stock_price(real_stock_symbols[i], start_date, end_date)$adjusted, error=function(e) NULL))})
warnings = warnings()


# obtain the real_stock_prices
real_stock_prices = data.frame(stock_prices)
colnames(real_stock_prices) = real_stock_symbols
row.names(real_stock_prices) = dates

# test
test_that("stock prices are correct",{
  expect_equal(real_stock_prices$DLR, one_stock_price("DLR", start_date, end_date)$adjusted)
  expect_equal(real_stock_prices$AAPL, one_stock_price("AAPL", start_date, end_date)$adjusted)
  expect_equal(real_stock_prices$NSC, one_stock_price("NSC", start_date, end_date)$adjusted)
})

# export
write.csv(real_stock_prices,
          paste0(folder_path, data_path, 
                 paste0(date_path, '_stock_prices.csv')),
          row.names = TRUE)






# calculate and save log-return data
real_stock_returns = data.frame(
  sapply(1:dim(real_stock_prices)[2], 
         function(i){
           100 * (log(real_stock_prices[,i][-1]) - log(real_stock_prices[,i][-dim(real_stock_prices)[1]]))}))
colnames(real_stock_returns) = real_stock_symbols
row.names(real_stock_prices) = dates

# test
test_that("stock returns are correct",{
  expect_equal(real_stock_returns[3,10], 100*(log(real_stock_prices[4,10])-log(real_stock_prices[3,10])))
  expect_equal(real_stock_returns[100,200], 100*(log(real_stock_prices[101,200])-log(real_stock_prices[100,200])))
  expect_equal(real_stock_returns[249,450], 100*(log(real_stock_prices[250,450])-log(real_stock_prices[249,450])))
})

# export
write.csv(real_stock_returns,
          paste0(folder_path, data_path, 
                 paste0(date_path, '_stock_returns.csv')),
          row.names = TRUE)
