#Statistical Significance

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"
#import scipy.fftpack

plt.rcParams["figure.figsize"] = (15,7.5)
plt.rcParams.update({'font.size': 20})
plt.rcParams["legend.fontsize"] = (15)


# read in the fft data
fft = pd.read_csv("grafana_data_export oct_fftcb.csv", sep = ';', header = 1)
fft


# reduce the time variable
fft.Time.str[11:19]

# replace time variable with reduced string
fft['Time'] = fft.Time.str[11:19]

# separate data into bands
fft_band0 = fft.loc[fft["Series"] == "CB FFT Band 0"]
fft_band1 = fft.loc[fft["Series"] == "CB FFT Band 1"]
fft_band2 = fft.loc[fft["Series"] == "CB FFT Band 2"]
fft_band3 = fft.loc[fft["Series"] == "CB FFT Band 3"]
fft_band4 = fft.loc[fft["Series"] == "CB FFT Band 4"]
fft_band5 = fft.loc[fft["Series"] == "CB FFT Band 5"]
fft_band6 = fft.loc[fft["Series"] == "CB FFT Band 6"]
fft_band7 = fft.loc[fft["Series"] == "CB FFT Band 7"]

# resetting the indecies
fft_band0 = fft_band0.reset_index(drop=True)
fft_band1 = fft_band1.reset_index(drop=True)
fft_band2 = fft_band2.reset_index(drop=True)
fft_band3 = fft_band3.reset_index(drop=True)
fft_band4 = fft_band4.reset_index(drop=True)
fft_band5 = fft_band5.reset_index(drop=True)
fft_band6 = fft_band6.reset_index(drop=True)
fft_band7 = fft_band7.reset_index(drop=True)


#
#print("Indexes for B1:");
fft_band0.index[fft_band0['Time'] == '09:25:50']
fft_band0.index[fft_band0['Time'] == '09:30:50']
#print("Indexes for B2:")
fft_band0.index[fft_band0['Time'] == '09:37:00']
fft_band0.index[fft_band0['Time'] == '09:41:40']
#print("Indexes for B3:")
fft_band0.index[fft_band0['Time'] == '09:56:00']
fft_band0.index[fft_band0['Time'] == '10:00:40']
#print("Indexes for A1:");
fft_band0.index[fft_band0['Time'] == '16:00:00']
fft_band0.index[fft_band0['Time'] == '16:02:00']
#print("Indexes for A2:");
fft_band0.index[fft_band0['Time'] == '16:10:00']
fft_band0.index[fft_band0['Time'] == '16:14:00']
#print("Indexes for A3:");
fft_band0.index[fft_band0['Time'] == '16:19:00']
fft_band0.index[fft_band0['Time'] == '16:22:10']
#print("Indexes for A4:");
fft_band0.index[fft_band0['Time'] == '16:24:20']
fft_band0.index[fft_band0['Time'] == '16:28:00']
#print("Indexes for A5:");
fft_band0.index[fft_band0['Time'] == '16:31:30']
fft_band0.index[fft_band0['Time'] == '16:36:50']
#print("Indexes for A6:");
fft_band0.index[fft_band0['Time'] == '16:45:20']
fft_band0.index[fft_band0['Time'] == '16:50:50']
#print("Indexes for A7:");
fft_band0.index[fft_band0['Time'] == '16:57:10']
fft_band0.index[fft_band0['Time'] == '17:00:00']
print("Indexes for A8:",
fft_band0.index[fft_band0['Time'] == '17:00:00'],
fft_band0.index[fft_band0['Time'] == '17:05:30']);