
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from numpy.random import RandomState
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import adfuller
from scipy import signal
from scipy import stats
from statsmodels.tsa.api import VAR
from statsmodels.tools.eval_measures import rmse, aic
import pickle
from statsmodels.stats.stattools import durbin_watson
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.stattools import grangercausalitytests

def cross_corr_coef(lag_time_series, lead_time_series, lag):
    # calculate the cross correlation between two time series
    # if the result is not zero, then 'lead_time_series' leads 'lag_time_series'

    lag_time_series = lag_time_series.iloc[lag:]
    corr_coef = np.corrcoef(lag_time_series, lead_time_series.iloc[0:((lead_time_series.size)-lag)])[0][1]

    return corr_coef

def create_statistics(label, rolling_window, return_csv_location, price_csv_location):

    return_df = pd.read_csv(return_csv_location, index_col=[0])
    return_df_series1 = return_df.iloc[:, ::2]
    return_df_series2 = return_df.iloc[:, 1::2]

    return_mean1 = return_df_series1.mean(axis=0)
    sd1 = return_df_series1.std(axis=0)
    skew1 = return_df_series1.skew(axis=0)
    kurtosis1 = return_df_series1.kurtosis(axis=0)
    autocorrelation_return1 = return_df_series1.apply(lambda x: x.autocorr(lag=1))
    rolling_window = rolling_window
    rolling_return_sd1 = return_df_series1.apply(lambda x: x.rolling(rolling_window).std()).iloc[rolling_window + 1:]
    autocorrelation_return_rolling_sd1 = rolling_return_sd1.apply(lambda x: x.autocorr(lag=1))

    standardised_price_df1 = 100 * np.exp(return_df_series1.cumsum() / 100)
    standardised_price_df1.loc[-1] = list(np.full(len(standardised_price_df1.columns), 100))  # adding a row
    standardised_price_df1.index = standardised_price_df1.index + 1  # shifting index
    standardised_price_df1 = standardised_price_df1.sort_index()
    standardised_price_mean1 = np.array(standardised_price_df1.mean(axis=0))

    return_mean2 = return_df_series2.mean(axis=0)
    sd2 = return_df_series2.std(axis=0)
    skew2 = return_df_series2.skew(axis=0)
    kurtosis2 = return_df_series2.kurtosis(axis=0)
    autocorrelation_return2 = return_df_series2.apply(lambda x: x.autocorr(lag=1))
    rolling_return_sd2 = return_df_series2.apply(lambda x: x.rolling(rolling_window).std()).iloc[rolling_window + 1:]
    autocorrelation_return_rolling_sd2 = rolling_return_sd2.apply(lambda x: x.autocorr(lag=1))

    standardised_price_df2 = 100 * np.exp(return_df_series2.cumsum() / 100)
    standardised_price_df2.loc[-1] = list(np.full(len(standardised_price_df2.columns), 100))  # adding a row
    standardised_price_df2.index = standardised_price_df2.index + 1  # shifting index
    standardised_price_df2 = standardised_price_df2.sort_index()
    standardised_price_mean2 = np.array(standardised_price_df2.mean(axis=0))


    # adf test on original prices: test if the price difference of the two time series is stationary
    price_df = pd.read_csv(price_csv_location, index_col=[0])
    price_df_series1 = price_df.iloc[:, ::2]
    price_df_series2 = price_df.iloc[:, 1::2]
    p_values = []
    for i in range(248):
        reg = LinearRegression().fit(np.array(price_df_series1.iloc[:, i]).reshape((-1, 1)), np.array(price_df_series2.iloc[:, i]))
        y_pred = reg.predict(np.array(price_df_series1.iloc[:, i]).reshape((-1, 1)))
        res = np.array(price_df_series2.iloc[:, i]) - y_pred
        adf_result = adfuller(res)[1]
        p_values.append(adf_result)
    p_values = pd.Series(p_values)


    # Cross-correlation between series
    corr_ts1_lag_0 = []
    corr_ts1_lag_1 = []
    corr_ts1_lag_2 = []
    corr_ts1_lag_3 = []
    corr_ts2_lag_1 = []
    corr_ts2_lag_2 = []
    corr_ts2_lag_3 = []
    for i in range(248):
        corr_ts1_lag_0.append(cross_corr_coef(return_df_series1.iloc[:, i], return_df_series2.iloc[:, i], 0))
        corr_ts1_lag_1.append(cross_corr_coef(return_df_series1.iloc[:, i], return_df_series2.iloc[:, i], 1))
        corr_ts1_lag_2.append(cross_corr_coef(return_df_series1.iloc[:, i], return_df_series2.iloc[:, i], 2))
        corr_ts1_lag_3.append(cross_corr_coef(return_df_series1.iloc[:, i], return_df_series2.iloc[:, i], 3))
        corr_ts2_lag_1.append(cross_corr_coef(return_df_series1.iloc[:, i], return_df_series2.iloc[:, i], 1))
        corr_ts2_lag_2.append(cross_corr_coef(return_df_series1.iloc[:, i], return_df_series2.iloc[:, i], 2))
        corr_ts2_lag_3.append(cross_corr_coef(return_df_series1.iloc[:, i], return_df_series2.iloc[:, i], 3))

    corr_ts1_lag_0 = pd.Series(corr_ts1_lag_0)
    corr_ts1_lag_1 = pd.Series(corr_ts1_lag_1)
    corr_ts1_lag_2 = pd.Series(corr_ts1_lag_2)
    corr_ts1_lag_3 = pd.Series(corr_ts1_lag_3)
    corr_ts2_lag_1 = pd.Series(corr_ts2_lag_1)
    corr_ts2_lag_2 = pd.Series(corr_ts2_lag_2)
    corr_ts2_lag_3 = pd.Series(corr_ts2_lag_3)


    ### Granger Causality test
    durbin_watson_statistic1 = []
    durbin_watson_statistic2 = []
    co_integration_statistic = []
    ts2_granger_cause_ts1 = []
    ts1_granger_cause_ts2 = []
    for i in range(248):
        ts1 = price_df_series1.iloc[:, i]
        ts2 = price_df_series2.iloc[:, i]
        bivariate_time_series = np.array(pd.DataFrame([ts1, ts2]).transpose())
        var_model = VAR(bivariate_time_series)
        var_result_aic = []

        for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            var_model_fit = var_model.fit(j)
            var_result_aic.append(var_model_fit.aic)

        var_lag = np.where(var_result_aic == np.min(var_result_aic))[0][0] + 1
        our_var_model = VAR(bivariate_time_series)
        our_var_model_fitted = our_var_model.fit(var_lag)

        # durbin_watson_statistic detect the presence of autocorrelation at lag 1 in the residuals from the regression
        durbin_watson_statistic = durbin_watson(our_var_model_fitted.resid)
        durbin_watson_statistic1.append(durbin_watson_statistic[0])
        durbin_watson_statistic2.append(durbin_watson_statistic[1])

        # test if the two time series co-integrated
        co_integration_statistic.append(ts.coint(ts1, ts2)[1])

        # granger causality test, output p-value of the F-test
        # For ts2_granger_cause_ts1, if p-value is less than 0.05, ts2 granger causes ts1, that is, the past values of ts2 have a statistically significant effect on the current value of ts1
        bivariate_ts1_ts2 = np.array(pd.DataFrame([ts1, ts2]).transpose())
        bivariate_ts2_ts1 = np.array(pd.DataFrame([ts2, ts1]).transpose())
        ts2_granger_cause_ts1.append(grangercausalitytests(bivariate_ts1_ts2, [var_lag])[var_lag][0]["ssr_ftest"][1])
        ts1_granger_cause_ts2.append(grangercausalitytests(bivariate_ts2_ts1, [var_lag])[var_lag][0]["ssr_ftest"][1])

    durbin_watson_statistic1 = pd.Series(durbin_watson_statistic1)
    durbin_watson_statistic2 = pd.Series(durbin_watson_statistic2)
    co_integration_statistic = pd.Series(co_integration_statistic)
    ts2_granger_cause_ts1 = pd.Series(ts2_granger_cause_ts1)
    ts1_granger_cause_ts2 = pd.Series(ts1_granger_cause_ts2)


    ### create new statistics data frame
    new_statistics = pd.DataFrame([
        standardised_price_mean1, standardised_price_mean2,
        return_mean1, return_mean2,
        sd1, sd2,
        skew1, skew2,
        kurtosis1, kurtosis2,
        autocorrelation_return1, autocorrelation_return2,
        autocorrelation_return_rolling_sd1, autocorrelation_return_rolling_sd2,
        p_values,
        corr_ts1_lag_0,
        corr_ts1_lag_1, corr_ts1_lag_2, corr_ts1_lag_3,
        corr_ts2_lag_1, corr_ts2_lag_2, corr_ts2_lag_3,
        durbin_watson_statistic1, durbin_watson_statistic2, co_integration_statistic,
        ts2_granger_cause_ts1, ts1_granger_cause_ts2
        ])
    new_statistics = new_statistics.transpose()
    new_statistics.columns = [
        'standardised_price_mean1', 'standardised_price_mean2',
        'return_mean1', 'return_mean2',
        'return_sd1', 'return_sd2',
        'return_skew1', 'return_skew2',
        'return_kurtosis1', 'return_kurtosis2',
        'return_autocorrelation1', 'return_autocorrelation2',
        'return_autocorrelation_rolling_sd1', 'return_autocorrelation_rolling_sd2',
        'price_adf_p_values',
        'return_correlation_ts1_lag_0',
        'return_correlation_ts1_lag_1', 'return_correlation_ts1_lag_2', 'return_correlation_ts1_lag_3',
        'return_correlation_ts2_lag_1', 'return_correlation_ts2_lag_2', 'return_correlation_ts2_lag_3',
        'durbin_watson_statistic1', 'durbin_watson_statistic2', 'co_integration_statistic',
        'ts2_granger_cause_ts1', 'ts1_granger_cause_ts2']
    label_col_position = new_statistics.shape[1]
    new_statistics.insert(label_col_position, 'label', label, allow_duplicates=True)

    return new_statistics

def create_train_test_data(real_data, simulated_data, proportion):

    rs1 = RandomState(123)
    num_total_rows = len(real_data)
    num_train_rows = int(num_total_rows * proportion)  # 75% of the real_data

    random_real_train_indices = rs1.choice(num_total_rows, num_train_rows, replace=False)
    train_real = real_data.iloc[random_real_train_indices, :]
    test_real = real_data.iloc[np.delete(range(num_total_rows), random_real_train_indices), :]

    rs2 = RandomState(1234)
    random_simulated_train_indices = rs2.choice(num_total_rows, num_train_rows, replace=False)
    train_simulated = simulated_data.iloc[random_simulated_train_indices, :]
    test_simulated = simulated_data.iloc[np.delete(range(num_total_rows), random_simulated_train_indices), :]

    rs3 = RandomState(12345)
    rs4 = RandomState(123456)
    train = pd.concat([train_real, train_simulated])
    train = train.iloc[rs3.choice(len(train), len(train), replace=False), :]  #
    test = pd.concat([test_real, test_simulated])
    test = test.iloc[rs4.choice(len(test), len(test), replace=False), :]  #

    num_cols = real_data.shape[1] - 1
    x_train = train.iloc[:, 0:num_cols]  # (744, 6) (x_train.shape)
    y_train = train.iloc[:, num_cols]  # (744, )
    x_test = test.iloc[:, 0:num_cols]  # (248, 6)
    y_test = test.iloc[:, num_cols]  # (248, )
    return x_train, y_train, x_test, y_test


real_statistics = create_statistics(label="real", rolling_window=20, return_csv_location="/Users/changmao/Desktop/real_pair_returns.csv", price_csv_location="~/Desktop/real_pair_prices.csv")
simulated_statistics = create_statistics(label="simulated", rolling_window=20, return_csv_location="/Users/changmao/Desktop/simulated_pair_returns.csv", price_csv_location="~/Desktop/simulated_pair_prices.csv")
X_train, y_train, X_test, y_test = create_train_test_data(real_statistics, simulated_statistics, 0.75)


random.seed(123)
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score
from supervised.preprocessing.eda import EDA
automl = AutoML(eval_metric='accuracy')
automl.fit(X_train, y_train)
predictions = automl.predict(X_test)
print(f"Accuracy of predictions:  {accuracy_score(y_test,predictions):.3f}")

# EDA.extensive_eda(X_train, y_train, save_path="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Return series classifier/AutoML...")
# globals().clear()
######################################################################

