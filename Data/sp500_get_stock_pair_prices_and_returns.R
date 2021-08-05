# This file presents how to group the historical adjusted closing prices of stocks in S&P 500 during 'start_date' and 'end_date' into pairs using the cointegration method.
# Before running this file, you should use "sp500_get_stock_prices_and_returns.csv" to get historical prices and returns for the time period you want.
# The following "folder_path" is where the author saves the data file in a personal computer. You can set the 'folder_path' as where you download the project folder.
# Also, you should set the 'start_date' and 'end_date' the same as you did in "sp500_get_stock_prices_and_returns.csv" file and then the following codes can be run smoothly.

folder_path = "/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub"
data_path = "/Summer-Research-Project/Data/"
start_date = "2018-01-01"
end_date = "2018-12-31"
date_path = paste('sp500', gsub('-','',start_date), gsub('-','',end_date), sep='_')



library(tseries)
library(tidyquant)
library(tidyverse) 
real_stock_prices = read.csv(paste0(folder_path, data_path, 
                                    paste0(date_path, '_stock_prices.csv')), 
                             row.names=1)

dates = tq_get("AAPL", from=start_date, to=end_date)$date
row.names(real_stock_prices) = dates


# Test if the price of each stock is stationary. In other words, find out the order of integration of each stock price series.


# There are a total of n(n-1)/2 stock pair combinations, in this case, n=496, hence 122760 combinations. For each pair combination, we fit a linear regression model to the pair prices and extract errors from the model then test if the error series is stationary, literally we are testing if the two prices series are cointegrated. Similarly, the test can be carried out using the "adf.test" and we will then rank the pairs by the p-values, the lower p-value, the higher rank namely they are cointegrated.


p_value_matrix = matrix(0, dim(real_stock_prices)[2], dim(real_stock_prices)[2]) # 122760
p_value_vector = c()
position_vector = c()

for (i in 1:(dim(real_stock_prices)[2]-1)){
  
  for (j in (i+1):dim(real_stock_prices)[2]){
    
    fit = lm(real_stock_prices[,i] ~ real_stock_prices[,j])
    res = as.numeric(fit$residuals)
    p_value = adf.test(res)$p.value
    p_value_matrix[i,j] = p_value
    
    p_value_vector = c(p_value_vector, p_value)
    position_vector = c(position_vector, paste0("row", i, "column", j))
  }
}
warnings = warnings()
stock = tq_index("SP500")
stock_symbols = stock$symbol
real_stock_symbols = stock_symbols[-c(match(c("BRK.B","DOW","CARR","OTIS","CTVA","BF.B","FOXA","OGN","FOX", "VSCO"),stock_symbols))]
colnames(p_value_matrix) = real_stock_symbols
row.names(p_value_matrix) = real_stock_symbols



write.csv(p_value_matrix, paste0(folder_path, data_path, paste0(date_path, "_p_value_matrix.csv")), row.names = TRUE)
write.csv(p_value_vector, paste0(folder_path, data_path, paste0(date_path, "_p_value_vector.csv")))
write.csv(position_vector, paste0(folder_path, data_path, paste0(date_path, "_position_vector.csv")))

# p_value_matrix = read.csv(paste0(folder_path, data_path, paste0(date_path, "_p_value_matrix.csv")), row.names=1)
# p_value_vector = read.csv(paste0(folder_path, data_path, paste0(date_path, "_p_value_vector.csv")), row.names=1)
# position_vector = read.csv(paste0(folder_path, data_path,paste0(date_path, "_position_vector.csv")), row.names=1)


# randomly choose the pair stocks that give p_value 0.01
num = c()
for (i in 1:dim(p_value_matrix)[2]){
  num = c(num, sum(p_value_matrix[i,]==0.01))}
num # identify those have few 0.01 p_value with other stocks


pair_stocks = c()

while(dim(p_value_matrix)[1] > 1){
  
  positive_p_values = p_value_matrix[p_value_matrix>0]
  smallest_p_value = min(positive_p_values)
  
  for (i in 1:(dim(p_value_matrix)[1]-1)){
    row = p_value_matrix[i,]
    row = row[row>0]
    
    if (min(row)==smallest_p_value){
      position = match(min(row), p_value_matrix[i,])
      column_names = colnames(p_value_matrix)
      new_pair = c(column_names[i], column_names[position])
      pair_stocks = rbind(pair_stocks, new_pair)
      
      p_value_matrix = p_value_matrix[-c(i, position), -c(i, position)]
      break
    }
  }
}

pair_stocks = data.frame(pair_stocks)
p_value_matrix = read.csv(paste0(folder_path, data_path, paste0(date_path, "_p_value_matrix.csv")), row.names=1)

p_values = c()
for (i in 1:dim(pair_stocks)[1]){
  p_values = c(p_values, p_value_matrix[pair_stocks[i,1], pair_stocks[i,2]])
}
pair_stocks_values = cbind(pair_stocks, p_values)

write.csv(pair_stocks_values, paste0(folder_path, data_path, paste0(date_path, "_pair_stocks_values.csv")), row.names = TRUE)
# pair_stocks_values = read.csv(paste0(folder_path, data_path, paste0(date_path, "_pair_stocks_values.csv")), row.names=1)

# pair_stocks = pair_stocks_values[,1:2]

i = 1
i_vec = c()
real_pair_prices = data.frame(matrix(0, nrow=dim(real_stock_prices)[1], ncol=dim(real_stock_prices)[2]))
while (i <= dim(pair_stocks)[1]){
  
  print(i)
  i_vec = c(i_vec, i)
  pair_names = as.character(pair_stocks[i,])
  pair_cols  = match(pair_names, colnames(real_stock_prices))
  data1 = real_stock_prices[,pair_cols[1]]
  data2 = real_stock_prices[,pair_cols[2]]
  data = data.frame(data1, data2)

  real_pair_prices[, (2*i-1):(2*i)] = data
  i = i + 1
}
colnames(real_pair_prices) = unlist(t(pair_stocks))
row.names(real_pair_prices) = dates
write.csv(real_pair_prices, 
          paste0(folder_path, data_path, 
                 paste(date_path, "real_pair_prices.csv", sep='_')), 
          row.names = TRUE)

real_pair_returns = data.frame(sapply(1:dim(real_pair_prices)[2], function(i){
  100 * (log(real_pair_prices[,i][-1]) - log(real_pair_prices[,i][-dim(real_pair_prices)[1]]))}))

write.csv(real_pair_returns, paste0(folder_path, data_path, "real_pair_returns.csv"), row.names = TRUE)
write.csv(i_vec, paste0(folder_path, data_path, "i_vec.csv"), row.names = TRUE)

