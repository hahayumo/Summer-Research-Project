import pandas as pd
import numpy as np
from datetime import datetime


file_folder_path = "/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Param calibration/Cluster jobs/ou88_simstudy/"
file1 = pd.read_csv(file_folder_path+"ou88_sim_jumbo20_1_result.csv", index_col=[0])
file2 = pd.read_csv(file_folder_path+"ou88_sim_jumbo120_2_result.csv", index_col=[0])
file3 = pd.read_csv(file_folder_path+"ou88_sim_jumbo120_3_result.csv", index_col=[0])
file4 = pd.read_csv(file_folder_path+"ou88_sim_jumbo120_4_result.csv", index_col=[0])
file5 = pd.read_csv(file_folder_path+"ou88_sim_jumbo120_5_result.csv", index_col=[0])
csv_file = pd.concat([file1, file2, file3, file4, file5])


csv_file = pd.read_csv(file_folder_path+"ou88_sim_jumbo20_1_result.csv", index_col=[0])


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

    resx = pd.DataFrame(csv_file.iloc[:, 0].apply(resx_clean).tolist(), columns=['mu11', 'mu12', 'mu21', 'mu22',
                                                                                 'sigma11', 'sigma12', 'sigma21', 'sigma22'])
    time = pd.DataFrame(csv_file.iloc[:, 1].apply(time_clean).tolist(), columns=['time'])
    loss = pd.DataFrame(csv_file.iloc[:, 2].apply(loss_clean).tolist(), columns=['loss'])
    new_data = pd.concat([resx, time, loss], axis=1)
    return new_data


clean_data = data_clean(csv_file)
mean_data = clean_data.mean(axis=0)
std_data = clean_data.std(axis=0)
print(mean_data)
print(std_data)
# 8 True params:
mu11, mu12, mu21, mu22 = 5.0114, 1.1836, 3.3541, 0.9061
sigma11, sigma12, sigma21, sigma22 = -3.4211, -1.4282, -2.1742, -1.3767
