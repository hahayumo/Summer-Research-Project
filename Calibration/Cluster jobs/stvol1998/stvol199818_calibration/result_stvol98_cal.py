import pandas as pd
import numpy as np
from datetime import datetime


file_folder_path = "/Users/changmao/Desktop/OneDrive - Imperial College London/InferStat - MSc Summer Project/GitHub/Summer-Research-Project/Calibration/Cluster jobs/stvol1998/stvol199818_calibration/"
file1 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_1_result.csv", index_col=[0])
#file2 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_2_result.csv", index_col=[0])
#file3 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_3_result.csv", index_col=[0])
file4 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_4_result.csv", index_col=[0])
file5 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_5_result.csv", index_col=[0])
#file6 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_6_result.csv", index_col=[0])
file7 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_7_result.csv", index_col=[0])
#file8 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_8_result.csv", index_col=[0])
file9 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_9_result.csv", index_col=[0])
file10 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_10_result.csv", index_col=[0])
file11 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_11_result.csv", index_col=[0])
file12 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_12_result.csv", index_col=[0])
file13 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_13_result.csv", index_col=[0])
#file14 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_14_result.csv", index_col=[0])
file15 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_15_result.csv", index_col=[0])
file16 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_16_result.csv", index_col=[0])
file17 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_17_result.csv", index_col=[0])
file18 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_18_result.csv", index_col=[0])
file19 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_19_result.csv", index_col=[0])
#file20 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_20_result.csv", index_col=[0])
file21 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_21_result.csv", index_col=[0])
file22 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_22_result.csv", index_col=[0])
file23 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_23_result.csv", index_col=[0])
file24 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_24_result.csv", index_col=[0])
file25 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_25_result.csv", index_col=[0])
file26 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_26_result.csv", index_col=[0])
file27 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_27_result.csv", index_col=[0])
file28 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_28_result.csv", index_col=[0])
file29 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_29_result.csv", index_col=[0])
file30 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_30_result.csv", index_col=[0])
file31 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_31_result.csv", index_col=[0])
#file32 = pd.read_csv(file_folder_path + "stvol98_cal_medium16_32_result.csv", index_col=[0])



csv_file = pd.concat([
    file1, file4, file5, file7, file9, file10,
    file11, file12, file13, file15, file16, file17, file18, file19,
    file21, file22, file23, file24, file25, file26, file27, file28, file29, file30,
    file31])




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

    resx = pd.DataFrame(csv_file.iloc[:, 0].apply(resx_clean).tolist(), columns=[
        'mu11', 'mu21', 'mu22', 'mu31', 'mu41', 'mu42',
        'sigma11', 'sigma12', 'sigma13', 'sigma14',
        'sigma21', 'sigma22', 'sigma23', 'sigma24',
        'sigma31', 'sigma32', 'sigma33', 'sigma34',
        'sigma41', 'sigma42', 'sigma43', 'sigma44'])
    time = pd.DataFrame(csv_file.iloc[:, 1].apply(time_clean).tolist(), columns=['time'])
    loss = pd.DataFrame(csv_file.iloc[:, 2].apply(loss_clean).tolist(), columns=['loss'])
    new_data = pd.concat([resx, time, loss], axis=1)
    return new_data


clean_data = data_clean(csv_file)

mean_data = clean_data.mean(axis=0)
std_data = clean_data.std(axis=0)
print(mean_data)
print(std_data)
