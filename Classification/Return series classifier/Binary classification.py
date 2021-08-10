
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_statistics(label, rolling_window, csv_location):

    return_df = pd.read_csv(csv_location)
    sd = return_df.std(axis=0)
    skew = return_df.skew(axis=0)
    kurtosis = return_df.kurtosis(axis=0)
    autocorrelation_return = return_df.apply(lambda x: x.autocorr(lag=1))
    rolling_window = rolling_window
    rolling_return_sd = return_df.apply(lambda x: x.rolling(rolling_window).std()).iloc[rolling_window + 1:]
    autocorrelation_return_rolling_sd = rolling_return_sd.apply(lambda x: x.autocorr(lag=1))

    price_df = 100 * np.exp(return_df.cumsum() / 100)
    price_df.loc[-1] = list(np.full(len(price_df.columns), 100))  # adding a row
    price_df.index = price_df.index + 1  # shifting index
    price_df = price_df.sort_index()
    mean = price_df.mean(axis=0)

    new_statistics = pd.DataFrame([mean, sd, skew, kurtosis, autocorrelation_return, autocorrelation_return_rolling_sd])
    new_statistics = new_statistics.transpose()
    new_statistics.columns = ['mean', 'sd', 'skew', 'kurtosis', 'autocorrelation_return', 'autocorrelation_return_rolling_sd']
    new_statistics.insert(6, 'label', label, allow_duplicates=True)

    return new_statistics

real_data = create_statistics(label="real", rolling_window=20, csv_location="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/export return data/real_stock_returns.csv")
simulated_data = create_statistics(label="simulated", rolling_window=20, csv_location="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/export return data/n_sym_return_series.csv")

def create_train_test_data(real_data, simulated_data, proportion):

    num_total_rows = len(real_data)
    num_train_rows = int(num_total_rows * proportion)  # 75% of the real_data

    random_real_train_indices = np.random.choice(num_total_rows, num_train_rows, replace=False)
    train_real = real_data.iloc[random_real_train_indices, :]
    test_real = real_data.iloc[np.delete(range(num_total_rows), random_real_train_indices), :]

    random_simulated_train_indices = np.random.choice(num_total_rows, num_train_rows, replace=False)
    train_simulated = simulated_data.iloc[random_simulated_train_indices, :]
    test_simulated = simulated_data.iloc[np.delete(range(num_total_rows), random_simulated_train_indices), :]

    train = pd.concat([train_real, train_simulated])
    train = train.iloc[np.random.choice(len(train), len(train), replace=False), :]  #
    test = pd.concat([test_real, test_simulated])
    test = test.iloc[np.random.choice(len(test), len(test), replace=False), :]  #

    x_train = train.iloc[:, 0:6]  # (744, 6) (x_train.shape)
    y_train = train.iloc[:, 6]  # (744, )
    x_test = test.iloc[:, 0:6]  # (248, 6)
    y_test = test.iloc[:, 6]  # (248, )
    return x_train, y_train, x_test, y_test

X_train, y_train, X_test, y_test = create_train_test_data(real_data, simulated_data, 0.75)

import random
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score
from supervised.preprocessing.eda import EDA
automl = AutoML(eval_metric='accuracy')
automl.fit(X_train, y_train)
predictions = automl.predict(X_test)
print(f"Accuracy of predictions:  {accuracy_score(y_test,predictions):.3f}")

EDA.extensive_eda(X_train, y_train, save_path="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/AutoML_2")


######################################################################
# GBM
######################################################################
real_data = create_statistics(label="real", rolling_window=20, csv_location="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/export return data/real_stock_returns.csv")
simulated_heston_data = create_statistics(label="simulated", rolling_window=20, csv_location="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/trials/GBM_returns.csv")
X_train, y_train, X_test, y_test = create_train_test_data(real_data, simulated_heston_data, 0.75)
import random
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score
from supervised.preprocessing.eda import EDA
automl = AutoML(eval_metric='accuracy')
automl.fit(X_train, y_train)
predictions = automl.predict(X_test)
print(f"Accuracy of predictions:  {accuracy_score(y_test,predictions):.3f}")
EDA.extensive_eda(X_train, y_train, save_path="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/AutoML_5")
######################################################################
#
######################################################################


######################################################################
#
######################################################################


######################################################################
#
######################################################################


######################################################################
#
######################################################################


######################################################################

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import adfuller

def create_statistics(label, rolling_window, csv_location):

    return_df = pd.read_csv(csv_location, index_col=[0])
    return_df_series1 = return_df.iloc[:, ::2]
    return_df_series2 = return_df.iloc[:, 1::2]

    sd1 = return_df_series1.std(axis=0)
    skew1 = return_df_series1.skew(axis=0)
    kurtosis1 = return_df_series1.kurtosis(axis=0)
    autocorrelation_return1 = return_df_series1.apply(lambda x: x.autocorr(lag=1))
    rolling_window = rolling_window
    rolling_return_sd1 = return_df_series1.apply(lambda x: x.rolling(rolling_window).std()).iloc[rolling_window + 1:]
    autocorrelation_return_rolling_sd1 = rolling_return_sd1.apply(lambda x: x.autocorr(lag=1))

    price_df1 = 100 * np.exp(return_df_series1.cumsum() / 100)
    price_df1.loc[-1] = list(np.full(len(price_df1.columns), 100))  # adding a row
    price_df1.index = price_df1.index + 1  # shifting index
    price_df1 = price_df1.sort_index()
    mean1 = np.array(price_df1.mean(axis=0))

    sd2 = return_df_series2.std(axis=0)
    skew2 = return_df_series2.skew(axis=0)
    kurtosis2 = return_df_series2.kurtosis(axis=0)
    autocorrelation_return2 = return_df_series2.apply(lambda x: x.autocorr(lag=1))
    rolling_return_sd2 = return_df_series2.apply(lambda x: x.rolling(rolling_window).std()).iloc[rolling_window + 1:]
    autocorrelation_return_rolling_sd2 = rolling_return_sd2.apply(lambda x: x.autocorr(lag=1))

    price_df2 = 100 * np.exp(return_df_series2.cumsum() / 100)
    price_df2.loc[-1] = list(np.full(len(price_df2.columns), 100))  # adding a row
    price_df2.index = price_df2.index + 1  # shifting index
    price_df2 = price_df2.sort_index()
    mean2 = np.array(price_df2.mean(axis=0))

    p_values = []
    for i in range(248):
        reg = LinearRegression().fit(np.array(price_df1.iloc[:, i]).reshape((-1, 1)), np.array(price_df2.iloc[:, i]))
        y_pred = reg.predict(np.array(price_df1.iloc[:, i]).reshape((-1, 1)))
        res = np.array(price_df2.iloc[:, i]) - y_pred
        adf_result = adfuller(res)[1]
        p_values.append(adf_result)
    p_values = pd.Series(p_values)


    new_statistics = pd.DataFrame([mean1, mean2, sd1, sd2, skew1, skew2, kurtosis1, kurtosis2, autocorrelation_return1, autocorrelation_return2, autocorrelation_return_rolling_sd1, autocorrelation_return_rolling_sd2, p_values])
    new_statistics = new_statistics.transpose()
    new_statistics.columns = ['mean1', 'mean2', 'sd1', 'sd2', 'skew1', 'skew2', 'kurtosis1', 'kurtosis2', 'autocorrelation_return1', 'autocorrelation_return2', 'autocorrelation_return_rolling_sd1', 'autocorrelation_return_rolling_sd2', 'adf_p_values']
    new_statistics.insert(13, 'label', label, allow_duplicates=True)

    return new_statistics

real_data = create_statistics(label="real", rolling_window=20, csv_location="/Users/changmao/Desktop/real_pair_returns.csv")
simulated_data = create_statistics(label="simulated", rolling_window=20, csv_location="/Users/changmao/Desktop/simulated_pair_returns.csv")

def create_train_test_data(real_data, simulated_data, proportion):

    num_total_rows = len(real_data)
    num_train_rows = int(num_total_rows * proportion)  # 75% of the real_data

    random_real_train_indices = np.random.choice(num_total_rows, num_train_rows, replace=False)
    train_real = real_data.iloc[random_real_train_indices, :]
    test_real = real_data.iloc[np.delete(range(num_total_rows), random_real_train_indices), :]

    random_simulated_train_indices = np.random.choice(num_total_rows, num_train_rows, replace=False)
    train_simulated = simulated_data.iloc[random_simulated_train_indices, :]
    test_simulated = simulated_data.iloc[np.delete(range(num_total_rows), random_simulated_train_indices), :]

    train = pd.concat([train_real, train_simulated])
    train = train.iloc[np.random.choice(len(train), len(train), replace=False), :]  #
    test = pd.concat([test_real, test_simulated])
    test = test.iloc[np.random.choice(len(test), len(test), replace=False), :]  #

    num_cols = real_data.shape[1] - 1
    x_train = train.iloc[:, 0:num_cols]  # (744, 6) (x_train.shape)
    y_train = train.iloc[:, num_cols]  # (744, )
    x_test = test.iloc[:, 0:num_cols]  # (248, 6)
    y_test = test.iloc[:, num_cols]  # (248, )
    return x_train, y_train, x_test, y_test

X_train, y_train, X_test, y_test = create_train_test_data(real_data, simulated_data, 0.75)

import random
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score
from supervised.preprocessing.eda import EDA
automl = AutoML(eval_metric='accuracy')
automl.fit(X_train, y_train)
predictions = automl.predict(X_test)
print(f"Accuracy of predictions:  {accuracy_score(y_test,predictions):.3f}")

EDA.extensive_eda(X_train, y_train, save_path="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Return series classifier/AutoML...")
######################################################################























































