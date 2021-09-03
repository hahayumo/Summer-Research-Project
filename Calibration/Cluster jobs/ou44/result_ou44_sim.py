import pandas as pd
import numpy as np
from datetime import datetime


file_folder_path = "/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/ou44/"
file1 = pd.read_csv(file_folder_path + "ou44_jumbo48_1_result.csv", index_col=[0])
file2 = pd.read_csv(file_folder_path + "ou44_jumbo48_2_result.csv", index_col=[0])
file3 = pd.read_csv(file_folder_path + "ou44_jumbo48_3_result.csv", index_col=[0])
file4 = pd.read_csv(file_folder_path + "ou44_jumbo48_4_result.csv", index_col=[0])
file5 = pd.read_csv(file_folder_path + "ou44_jumbo48_5_result.csv", index_col=[0])
file6 = pd.read_csv(file_folder_path + "ou44_jumbo48_6_result.csv", index_col=[0])
file7 = pd.read_csv(file_folder_path + "ou44_jumbo48_7_result.csv", index_col=[0])
file8 = pd.read_csv(file_folder_path + "ou44_jumbo48_8_result.csv", index_col=[0])
file9 = pd.read_csv(file_folder_path + "ou44_jumbo48_9_result.csv", index_col=[0])
file10 = pd.read_csv(file_folder_path + "ou44_jumbo48_10_result.csv", index_col=[0])
file11 = pd.read_csv(file_folder_path + "ou44_jumbo20_11_result.csv", index_col=[0])

csv_file = pd.concat([file1, file2, file3, file4, file5, file6, file7, file8, file9, file10, file11])




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

clean_data = pd.concat([clean_data, pd.DataFrame(np.exp(clean_data.iloc[:, 2]))], axis=1)
clean_data = pd.concat([clean_data, pd.DataFrame(np.exp(clean_data.iloc[:, 3]))], axis=1)

mean_data = clean_data.mean(axis=0)
std_data = clean_data.std(axis=0)
print(mean_data)
print(std_data)

# 4 params are:
mu12, mu22, sigma11, sigma22 = 0.0557, 0.0196, -1.3349, -1.3200

