
n_sim_ou = function(random_seed, num_sim,
                    mu11, mu12, mu21, mu22, 
                    sigma11, sigma12, sigma21, sigma22,
                    xinit_vec, T0, T, length){
  
  set.seed(random_seed)
  
  drift = c("mu11-mu12*X1", "mu21-mu22*X2")
  diffusion = matrix(c("exp(sigma11)", "exp(sigma12)", "exp(sigma21)", "exp(sigma22)"), 2, 2, byrow=TRUE)
  ou_model = setModel(drift=drift, diffusion=diffusion, 
                      time.variable = "t",
                      state.var=c("X1","X2"), solve.variable=c("X1","X2"))
  
  newsamp = setSampling(Initial=T0, Terminal=T, n=length)
  
  n_sim_ou_data = data.frame(matrix(nrow=length+1, ncol=2*num_sim))
  for (i in 1:num_sim){
    ou_sim = simulate(ou_model, 
                      true.par=list(
                        mu11=mu11, mu12=mu12, mu21=mu21, mu22=mu22, 
                        sigma11=sigma11, sigma12=sigma12, sigma21=sigma21, sigma22=sigma22), 
                      xinit=xinit_vec[[i]], sampling=newsamp)
    original_data = ou_sim@data@original.data
    one_sim_ou = data.frame(original_data[,1], original_data[,2])
    colnames(one_sim_ou) = c('series1', 'series2')
    n_sim_ou_data[,  (2*i-1):(2*i)] = one_sim_ou
  }
  return(n_sim_ou_data)
}

n_pair_prices = read.csv("/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Generator/sp500_20180101_20181231_pair_prices.csv", row.names=1)
n_log_pair_prices = log(n_pair_prices)
xinit_vec = list()
for (i in 1:(dim(n_pair_prices)[2]/2)){
  xinit_vec[[i]] = as.numeric(n_log_pair_prices[1, (2*i-1):(2*i)])
}

library(yuima)
n_sim_ou_log_price = n_sim_ou(
  random_seed=9868, num_sim=248,
  mu11=0, mu12=0.0369, mu21=0, mu22=0.0405,
  sigma11=-1.4118, sigma12=-1000, sigma21=-1000, sigma22=-1.3574,
  xinit_vec=xinit_vec, T0=0, T=1, length=250)

