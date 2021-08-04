library(tidyquant)
library(tidyverse) 

stock = tq_index("SP500")
stock_symbols = stock$symbol
start_date = "2018-01-01"
end_date = "2018-12-31"
dates = tq_get("AAPL", from=start_date, to=end_date)$date
num_dates = length(dates)

one_stock_price = function(stock_symbol, start_date, end_date){
  tq_get(stock_symbol, from = start_date, to = end_date) %>% filter(!is.na(adjusted))}

stock_prices = sapply(1:length(stock_symbols), function(i){return(tryCatch(one_stock_price(stock_symbols[i], start_date, end_date)$adjusted, error=function(e) NULL))})
warnings = warnings()

real_stock_prices = data.frame(matrix(unlist(stock_prices), nrow=num_dates, byrow=FALSE))
real_stock_symbols = stock_symbols[-c(match(c("BRK.B","CARR","DOW","OTIS","CTVA","BF.B","FOXA","OGN","FOX", "VSCO"), stock_symbols))]

colnames(real_stock_prices) = real_stock_symbols
row.names(real_stock_prices) = dates
real_stock_prices = as.xts(real_stock_prices, date_col = dates)

write.csv(real_stock_prices,"/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Data/real_stock_prices_20180101_20190101.csv", row.names = TRUE)





a = read.csv("/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Data/real_stock_prices_20180101_20190101.csv", row.names=1)

x <- read.csv(url("https://github.com/hahayumo/Summer-Research-Project/tree/main/Data/real_stock_prices_20180101_20190101.csv"))

