
one_jumpou_NIG = function(random_seed,
                    mu11, mu12, mu21, mu22, 
                    sigma11, sigma12, sigma21, sigma22,
                    j11, j12, j21, j22,
                    alpha, beta1, beta2, delta0, mu1, mu2, 
                    lambda11, lambda12, lambda21, lambda22,
                    xinit, T0, T, length){
  
  set.seed(random_seed)
  
  drift = c("mu11-mu12*X1", "mu21-mu22*X2")
  diffusion = matrix(c("exp(sigma11)", "exp(sigma12)", "exp(sigma21)", "exp(sigma22)"), 2, 2, byrow=TRUE)
  jumpcoef = matrix(c("j11", "j12", "j21", "j22"), 2, 2, byrow=TRUE) 
  
  
  alpha = alpha
  beta = c(beta1, beta2)
  delta0 = delta0
  mu = c(mu1, mu2)
  Lambda = matrix(c(lambda11, lambda12, lambda21, lambda22), 2, 2, byrow=TRUE)
  
  
  ou_model = setModel(drift=drift, diffusion=diffusion, jump.coeff=jumpcoef, 
                      measure.type="code",
                      measure=list(df="rNIG(z, alpha, beta, delta0, mu, Lambda)"), 
                      time.variable = "t",
                      state.var=c("X1","X2"), solve.variable=c("X1","X2"))
  
  newsamp = setSampling(Initial=T0, Terminal=T, n=length)
  
  ou_sim = simulate(ou_model, 
                    true.par=list(
                      mu11=mu11, mu12=mu12, mu21=mu21, mu22=mu22, 
                      sigma11=sigma11, sigma12=sigma12, sigma21=sigma21, sigma22=sigma22,
                      j11=j11, j12=j12, j21=j21, j22=j22,
                      alpha=alpha, beta=beta, delta0=delta0, mu=mu, Lambda=Lambda), 
                    xinit=xinit, sampling=newsamp)
  original_data = ou_sim@data@original.data
  one_sim_bi_jump_diff = data.frame(original_data[,1], original_data[,2])

  return(one_sim_bi_jump_diff)
}


library(yuima)
one_sim_jumpou_log_price = one_jumpou_NIG(
  random_seed=9868,
  mu11=2.8, mu12=0.0369, mu21=3.5, mu22=0.0405,
  sigma11=-1.4118, sigma12=-2.5, sigma21=-4.5, sigma22=-3.2,
  j11=0.3, j12=0.2, j21=0.1, j22=0.2,
  alpha=2, beta1=0, beta2=0, delta0=0.55, mu1=0, mu2=0,
  lambda11=1, lambda12=0, lambda21=0, lambda22=1,
  xinit=c(2, 3), T0=0, T=1, length=250)

