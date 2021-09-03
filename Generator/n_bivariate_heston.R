
n_heston = function(random_seed, num_sim,
                    mu1, mu11, mu12, mu2, mu21, mu22, 
                    xi1, xi2,
                    sigma11, sigma12, sigma13, sigma14,
                    sigma21, sigma22, sigma23, sigma24,
                    sigma31, sigma32, sigma33, sigma34,
                    sigma41, sigma42, sigma43, sigma44,
                    xinit_vec, vinit_vec, T0, T, length){
  
  set.seed(random_seed)
  
  drift = c("mu1*X1", "mu11-mu12*v1", "mu2*X2", "mu21-mu22*v2")
  diffusion = matrix(c("sqrt(v1)*X1*sigma11", "sqrt(v1)*X1*sigma12", "sqrt(v1)*X1*sigma13", "sqrt(v1)*X1*sigma14", 
                       "xi1*sqrt(v1)*sigma21", "xi1*sqrt(v1)*sigma22", "xi1*sqrt(v1)*sigma23", "xi1*sqrt(v1)*sigma24", 
                       "sqrt(v2)*X2*sigma31", "sqrt(v2)*X2*sigma32", "sqrt(v2)*X2*sigma33", "sqrt(v2)*X2*sigma34", 
                       "xi2*sqrt(v2)*sigma41", "xi2*sqrt(v2)*sigma42", "xi2*sqrt(v2)*sigma43", "xi2*sqrt(v2)*sigma44"), 
                     4, 4, byrow=TRUE)
  
  heston_model = setModel(drift=drift, diffusion=diffusion,
                          time.variable = "t",
                          state.variable=c("X1", "v1", "X2", "v2"),
                          solve.variable=c("X1", "v1", "X2", "v2"))
  newsamp = setSampling(Initial=T0, Terminal=T, n=length)
  
  n_sim_data = data.frame(matrix(nrow=length+1, ncol=2*num_sim))
  for (i in 1:num_sim){
    heston_sim = simulate(heston_model, 
                          true.par=list(
                            mu1=mu1, mu11=mu11, mu12=mu12, 
                            mu2=mu2, mu21=mu21, mu22=mu22, 
                            xi1=xi1, xi2=xi2,
                            sigma11=sigma11, sigma12=sigma12, sigma13=sigma13, sigma14=sigma14,
                            sigma21=sigma21, sigma22=sigma22, sigma23=sigma23, sigma24=sigma24,
                            sigma31=sigma31, sigma32=sigma32, sigma33=sigma33, sigma34=sigma34,
                            sigma41=sigma41, sigma42=sigma42, sigma43=sigma43, sigma44=sigma44), 
                          xinit=c(xinit_vec[[i]][1], vinit_vec[[i]][1], xinit_vec[[i]][2], vinit_vec[[i]][2]), 
                          sampling=newsamp)
    original_data = heston_sim@data@original.data
    one_sim_heston = data.frame(original_data[,1], original_data[,3])
    colnames(one_sim_heston) = c('series1', 'series2')
    n_sim_data[, (2*i-1):(2*i)] = one_sim_heston
  }
  return(n_sim_data)
}

n_pair_prices = read.csv("/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Generator/sp500_20180101_20181231_pair_prices.csv", row.names=1)
n_pair_returns = read.csv("/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Generator/sp500_20180101_20181231_pair_returns.csv", row.names=1)
xinit_vec = list()
vinit_vec = list()
for (i in 1:(dim(n_pair_prices)[2]/2)){
  xinit_vec[[i]] = as.numeric(n_pair_prices[1, (2*i-1):(2*i)])
  vinit_vec[[i]] = c(sd(n_pair_returns[, 2*i-1]/100), sd(n_pair_returns[, 2*i]/100))
}




library(yuima)
n_heston_price = n_heston(
  random_seed=9868, num_sim=248,
  mu1=0.1, mu11=0.05, mu12=0.05, mu2=0.1, mu21=0.05, mu22=0.05, 
  xi1=0.03, xi2=0.02,
  sigma11=1, sigma12=1, sigma13=0, sigma14=0,
  sigma21=1, sigma22=1, sigma23=0, sigma24=0,
  sigma31=0, sigma32=0, sigma33=1, sigma34=1,
  sigma41=0, sigma42=0, sigma43=1, sigma44=1,
  xinit_vec=xinit_vec, vinit_vec=vinit_vec, T0=0, T=1, length=250)

