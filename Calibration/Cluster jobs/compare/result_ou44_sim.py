import pandas as pd
import numpy as np
from datetime import datetime

file_folder_path = "/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/compare/"


#csv_file = pd.concat([
#    pd.read_csv(file_folder_path+"ou46_jumbo50_1_result.csv", index_col=[0]),
#    pd.read_csv(file_folder_path+"ou46_jumbo50_2_result.csv", index_col=[0])])
#csv_file = pd.concat([
#    pd.read_csv(file_folder_path+"ou48_jumbo50_1_result.csv", index_col=[0]),
#    pd.read_csv(file_folder_path+"ou48_jumbo50_2_result.csv", index_col=[0])])
csv_file = pd.concat([
    pd.read_csv(file_folder_path+"ou410_jumbo50_1_result.csv", index_col=[0]),
    pd.read_csv(file_folder_path+"ou410_jumbo50_2_result.csv", index_col=[0])])
#csv_file = pd.concat([
#    pd.read_csv(file_folder_path+"ou410_jumbo50_noseed_1_result.csv", index_col=[0]),
#    pd.read_csv(file_folder_path+"ou410_jumbo50_noseed_1_result.csv", index_col=[0])])
#csv_file = pd.concat([
#    pd.read_csv(file_folder_path+"gbm44_jumbo50_1_result.csv", index_col=[0]),
#    pd.read_csv(file_folder_path+"gbm44_jumbo50_2_result.csv", index_col=[0])])


def resx_clean(resx_string):
    r1 = resx_string.replace('[', '').replace(']', '').split(' ')
    r2 = list(filter(None, r1))
    r3 = [float(i) for i in r2]
    return r3

def time_clean(time_string):
    r1 = time_string.split('.')[0].split('days')[1].replace(' ', '').split(':')
    r2 = [float(i) for i in r1]
    seconds = r2[0]*3600 + r2[1]*60 + r2[2]
    return seconds

def loss_clean(loss_string):
    r1 = float(loss_string)
    return r1

def data_clean(csv_file):

    resx = pd.DataFrame(csv_file.iloc[:, 0].apply(resx_clean).tolist(), columns=['mu12', 'mu22', 'sigma11', 'sigma22'])
    time = pd.DataFrame(csv_file.iloc[:, 1].apply(time_clean).tolist(), columns=['time'])
    loss = pd.DataFrame(csv_file.iloc[:, 2].apply(loss_clean).tolist(), columns=['loss'])
    new_data = pd.concat([resx, time, loss], axis=1)
    return new_data


clean_data = data_clean(csv_file)
mean_data = clean_data.mean(axis=0)
std_data = clean_data.std(axis=0)
print(mean_data)
print(std_data)
# True parameters
mu12, mu22, sigma11, sigma22 = 0.0369, 0.0405, -1.4118, -1.3574
