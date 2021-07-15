
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

return_df = pd.read_csv("/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/export return data/real_stock_returns.csv")

sd = return_df.std(axis=0)
skew = return_df.skew(axis=0)
kurtosis = return_df.kurtosis(axis=0)
autocorrelation_return = return_df.apply(lambda x: x.autocorr(lag=1))
rolling_window = 20
rolling_return_sd = return_df.apply(lambda x: x.rolling(rolling_window).std()).iloc[rolling_window+1:]
autocorrelation_return_rolling_sd = rolling_return_sd.apply(lambda x: x.autocorr(lag=1))


price_df = 100 * np.exp(return_df.cumsum() / 100)
price_df.loc[-1] = list(np.full(len(price_df.columns), 100)) # adding a row
price_df.index = price_df.index + 1  # shifting index
price_df = price_df.sort_index()
mean = price_df.mean(axis=0)


real_data = pd.DataFrame([mean, sd, skew, kurtosis, autocorrelation_return, autocorrelation_return_rolling_sd])
real_data = real_data.transpose().set
real_data.columns = ['mean', 'sd', 'skew', 'kurtosis', 'autocorrelation_return', 'autocorrelation_return_rolling_sd']
real_data.insert(6, 'label', 'real', allow_duplicates=True)


##################################################################################################################################

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
ax[0, 0].hist(real_data['mean'])
ax[0, 0].set_xlim(0, 300)
ax[0, 0].set_ylim(0, 150)

ax[0, 1].hist(simulated_data['mean'])
ax[0, 1].set_xlim(0, 300)
ax[0, 1].set_ylim(0, 150)

ax[1, 0].hist(real_data['sd'])
ax[1, 0].set_xlim(0, 5)
ax[1, 0].set_ylim(0, 200)

ax[1, 1].hist(simulated_data['sd'])
ax[1, 1].set_xlim(0, 5)
ax[1, 1].set_ylim(0, 200)



##################################################################################################################################

combined_data = pd.concat([real_data, simulated_data])
X = combined_data.iloc[:, 0:6] # 744
y = combined_data.iloc[:, 6]   # 248

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=9868) # 75% training + 25% test

##################################################################################################################################


import random
random.seed(9868)
num_total_rows = len(real_data)
num_train_rows = int(num_total_rows * 0.75) # 75% of the real_data

random_real_train_indices = np.random.choice(num_total_rows, num_train_rows, replace=False)
train_real = real_data.iloc[random_real_train_indices, :]
test_real = real_data.iloc[np.delete(range(num_total_rows), random_real_train_indices), :]

random_simulated_train_indices = np.random.choice(num_total_rows, num_train_rows, replace=False)
train_simulated = simulated_data.iloc[random_simulated_train_indices, :]
test_simulated = simulated_data.iloc[np.delete(range(num_total_rows), random_simulated_train_indices), :]

train = pd.concat([train_real, train_simulated])
train = train.iloc[np.random.choice(len(train), len(train), replace=False), :] #
test = pd.concat([test_real, test_simulated])
test = test.iloc[np.random.choice(len(test), len(test), replace=False), :] #

x_train = train.iloc[:, 0:6]  # (744, 6) (x_train.shape)
y_train = train.iloc[:, 6]    # (744, )
x_test = test.iloc[:, 0:6]    # (248, 6)
y_test = test.iloc[:, 6]      # (248, )

##################################################################################################################################
##################################################################################
# data from Victoire
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
real_data = create_statistics(label="real", rolling_window=20, csv_location="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/export return data/victoire_real_stock_returns.csv")
simulated_data = create_statistics(label="simulated", rolling_window=20, csv_location="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/export return data/victoire_simulated_returns.csv")
X_train, y_train, X_test, y_test = create_train_test_data(real_data, simulated_data, 0.75)
import random
from supervised.automl import AutoML
automl = AutoML()
automl.fit(X_train, y_train)
predictions = automl.predict(X_test)
pred_accuracy = sum(predictions==y_test) / len(y_test)
print(pred_accuracy) # 1.0
##################################################################################
##################################################################################
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
real_data = create_statistics(label="real", rolling_window=20, csv_location="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/export return data/real_stock_returns.csv")
simulated_data = create_statistics(label="simulated", rolling_window=20, csv_location="/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/R files/export return data/n_asym_return_series.csv")
X_train, y_train, X_test, y_test = create_train_test_data(real_data, simulated_data, 0.75)
import random
from supervised.automl import AutoML
automl = AutoML()
automl.fit(X_train, y_train)
predictions = automl.predict(X_test)
pred_accuracy = sum(predictions==y_test) / len(y_test)
print(pred_accuracy) # 1.0
##################################################################################
pred_accuracy = sum(predictions==y_test) / len(y_test)
print(pred_accuracy)
##################################################################################
from supervised.automl import AutoML # mljar-supervised

# train models with AutoML
automl = AutoML(mode="Compete")
automl.fit(X_train, y_train)

# compute the MSE on test data
predictions = automl.predict(X_test)
print("Test MSE:", accuracy_score(y_test, predictions))
##################################################################################

real_pair_returns = pd.read_csv("/Users/changmao/Desktop/real_pair_returns.csv", index_col=[0])
real_pair_returns_series_1 = real_pair_returns.iloc[:, ::2] # series in the original columns 1,3,5,7,...
real_pair_returns_series_2 = real_pair_returns.iloc[:, 1::2] # series in the original columns 0,2,4,6,...
test_series_1 = real_pair_returns_series_1.iloc[:, 0]
test_series_2 = real_pair_returns_series_2.iloc[:, 0]
corr_matrix = np.corrcoef(test_series_1, test_series_2)
corr = corr_matrix[0][1]

def cross_corr_coef(lag_time_series, lead_time_series, lag):

    lag_time_series = lag_time_series.iloc[lag:]
    corr_coef = np.corrcoef(lag_time_series, lead_time_series.iloc[0:((lead_time_series.size)-lag)])[0][1]

    return corr_coef

corr_lag_0 = cross_corr_coef(test_series_1, test_series_2, 0)
corr_lag_1 = cross_corr_coef(test_series_1, test_series_2, 1)
corr_lag_2 = cross_corr_coef(test_series_1, test_series_2, 2)
corr_lag_3 = cross_corr_coef(test_series_1, test_series_2, 3)

corr_lag_0 = cross_corr_coef(test_series_2, test_series_1, 0)
corr_lag_1 = cross_corr_coef(test_series_2, test_series_1, 1)
corr_lag_2 = cross_corr_coef(test_series_2, test_series_1, 2)
corr_lag_3 = cross_corr_coef(test_series_2, test_series_1, 3)


##################################################################################





##################################################################################

##################################################################################