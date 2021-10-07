
library(tidyquant)
library(tidyverse) 

set.seed(9868)
stock = tq_index("SP500")
stock_symbols = stock$symbol
stock_symbols = stock_symbols[-c(match(c("BRK.B","CARR","OTIS","BBWI","BF.B","LUMN","OGN","FOX"), stock_symbols))]


first_series  = sample(x=stock_symbols, size=length(stock_symbols)%/%2, replace=FALSE)
second_series = stock_symbols[-match(first_series, stock_symbols)]
second_series = sample(x=second_series, size=length(second_series)-1, replace=FALSE)

pairs = data.frame(matrix(0, length(first_series), 2))
for (i in 1:length(first_series)){
  pairs[i, ] = c(first_series[i], second_series[i])}

random_start_end = function(){
  
  start_year  = sample(seq(2000, 2017, 1), 1)
  start_month = sample(seq(1, 12, 1), 1)
  start_day  = sample(seq(1, 28, 1), 1)
  start = paste(start_year, start_month, start_day, sep='-')
  end   = paste(start_year+2, start_month, start_day, sep='-')
  start_end = c(start, end)
  return(start_end)
}




pair_prices = data.frame(matrix(0, 1000, 500))
start_dates = data.frame(matrix(0, dim(pairs)[1], 1))


set.seed(1234)

for (i in 219:248){
  print('--------------------------------')
  print(i)
  start_end = random_start_end()
  print(start_end)
  
  first_price_series  = tryCatch(tq_get(pairs[i, 1], from=start_end[1], to=start_end[2])$adjusted, error=function(e) NULL)
  second_price_series = tryCatch(tq_get(pairs[i, 2], from=start_end[1], to=start_end[2])$adjusted, error=function(e) NULL)
  print(length(first_price_series))
  print(length(second_price_series))
  
  print('--------')
  j = 0
  while(length(first_price_series)<500 | length(second_price_series)<500){
    start_end = random_start_end()
    print(start_end[1])
    first_price_series  = tryCatch(tq_get(pairs[i, 1], from=start_end[1], to=start_end[2])$adjusted, error=function(e) NULL)
    second_price_series = tryCatch(tq_get(pairs[i, 2], from=start_end[1], to=start_end[2])$adjusted, error=function(e) NULL)
    print(length(first_price_series))
    print(length(second_price_series))
    j = j + 1
    if (j > 20){
      break
    }
  }

  if (length(first_price_series)<500 | length(second_price_series)<500){
    break
  }else{
    pair_prices[1:length(first_price_series), 2*i-1]  = first_price_series
    pair_prices[1:length(second_price_series), 2*i]   = second_price_series
    start_dates[i, ] = start_end[1]
  }  
}

# i=95 MRNA "2018-12-07"
# i=113 FOXA "2019-6-1"
# i=148 DOW "2019-3-20"
# i=177 
# i=218 CTVA "2019-5-24"

#pairs[i,]
#tq_get('CTVA',from='2000-1-1',tp='2020-1-1')
#start_end=c("2019-6-25","2021-6-25")




pair_prices_cal = pair_prices_cal[1:500, 1:496]
write.csv(pair_prices_cal,
          '/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_prices_cal.csv')
pair_prices_cal = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_prices_cal.csv', row.names = 1)

pair_returns_cal = data.frame(
  sapply(1:dim(pair_prices_cal)[2], 
         function(i){
           100 * (log(pair_prices_cal[,i][-1]) - log(pair_prices_cal[,i][-dim(pair_prices_cal)[1]]))}))
write.csv(pair_returns_cal,
          '/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_returns_cal.csv')
b = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_returns_cal.csv', row.names = 1)

pairs_cal = data.frame(pairs, start_dates)
write.csv(pairs_cal,
          '/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pairs_cal.csv')
pairs_cal = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pairs_cal.csv', row.names = 1)






pair_prices_classify = pair_prices[1:500, 1:496]
write.csv(pair_prices_classify,
          '/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_prices_classify.csv')
a = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_prices_classify.csv', row.names = 1)

pair_returns_classify = data.frame(
  sapply(1:dim(pair_prices_classify)[2], 
         function(i){
           100 * (log(pair_prices_classify[,i][-1]) - log(pair_prices_classify[,i][-dim(pair_prices_classify)[1]]))}))
write.csv(pair_returns_classify,
          '/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_returns_classify.csv')
b = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pair_returns_classify.csv', row.names = 1)

pairs_classify = data.frame(pairs, start_dates)
write.csv(pairs_classify,
          '/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pairs_classify.csv')
c = read.csv('/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/sp500_mixed_period_2000_2021/pairs_classify.csv', row.names = 1)
