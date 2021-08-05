# This file presents how to obtain the historical adjusted closing prices of each stock in S&P 500 during  'start_date' and 'end_date' using R package "tidyquant".
# You can set 'start_date' and 'end_date' as any available historical date that are of your interest and set the "folder_path" as where you download the project folder. The following "folder_path" is where the author saves the data file in a personal computer.

start_date = "2018-01-01"
end_date = "2018-12-31"
folder_path = "/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub"



library(tidyquant)
library(tidyverse) 
data_path = "/Summer-Research-Project/Data/"
date_path = paste('sp500', gsub('-','',start_date), gsub('-','',end_date), sep='_')

stock = tq_index("SP500")
stock_symbols = stock$symbol

dates = tq_get("AAPL", from=start_date, to=end_date)$date
num_dates = length(dates)

# extract the historical adjusted closing price data
one_stock_price = function(stock_symbol, start_date, end_date){
  tq_get(stock_symbol, from = start_date, to = end_date) %>% filter(!is.na(adjusted))}

stock_prices = sapply(1:length(stock_symbols), function(i){return(tryCatch(one_stock_price(stock_symbols[i], start_date, end_date)$adjusted, error=function(e) NULL))})
warnings = warnings()

real_stock_prices = data.frame(matrix(unlist(stock_prices), nrow=num_dates, byrow=FALSE))
real_stock_symbols = stock_symbols[-c(match(c("BRK.B","CARR","DOW","OTIS","CTVA","BF.B","FOXA","OGN","FOX", "VSCO"), stock_symbols))]

colnames(real_stock_prices) = real_stock_symbols
row.names(real_stock_prices) = dates

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

write.csv(real_stock_returns,
          paste0(folder_path, data_path, 
                 paste0(date_path, '_stock_returns.csv')),
          row.names = TRUE)
