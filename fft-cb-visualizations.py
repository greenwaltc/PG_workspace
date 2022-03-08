#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"
#import scipy.fftpack

plt.rcParams["figure.figsize"] = (15,7.5)
plt.rcParams.update({'font.size': 20})
plt.rcParams["legend.fontsize"] = (15)


# In[61]:


fft = pd.read_csv('grafana_data_export oct_fftcb.csv', sep=',', engine='python')
fft
#fft = pd.read_excel('grafana_data_export oct_fftcb_notscaled_excel.xlsx',  sheet_name='grafana_data_export oct_fftcb_n')


# In[62]:


fft['Time'] = fft.Time.str[11:19]


# In[63]:


fft_band0 = fft.loc[fft["Series"] == "CB FFT Band 0"]
fft_band1 = fft.loc[fft["Series"] == "CB FFT Band 1"]
fft_band2 = fft.loc[fft["Series"] == "CB FFT Band 2"]
fft_band3 = fft.loc[fft["Series"] == "CB FFT Band 3"]
fft_band4 = fft.loc[fft["Series"] == "CB FFT Band 4"]
fft_band5 = fft.loc[fft["Series"] == "CB FFT Band 5"]
fft_band6 = fft.loc[fft["Series"] == "CB FFT Band 6"]
fft_band7 = fft.loc[fft["Series"] == "CB FFT Band 7"]

fft_band0 = fft_band0.reset_index(drop=True)
fft_band1 = fft_band1.reset_index(drop=True)
fft_band2 = fft_band2.reset_index(drop=True)
fft_band3 = fft_band3.reset_index(drop=True)
fft_band4 = fft_band4.reset_index(drop=True)
fft_band5 = fft_band5.reset_index(drop=True)
fft_band6 = fft_band6.reset_index(drop=True)
fft_band7 = fft_band7.reset_index(drop=True)


# In[64]:


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
#print("Indexes for A8:");
fft_band0.index[fft_band0['Time'] == '17:00:00']
fft_band0.index[fft_band0['Time'] == '17:05:30'];


# In[65]:


#B1 Ads
b1_fft_band0 = fft_band0.iloc[1958:2720]
b1_fft_band1 = fft_band1.iloc[1950:2750]
b1_fft_band2 = fft_band2.iloc[1980:2750]
b1_fft_band3 = fft_band3.iloc[1969:2750]
b1_fft_band4 = fft_band4.iloc[1950:2750]
b1_fft_band5 = fft_band5.iloc[1950:2750]
b1_fft_band6 = fft_band6.iloc[1950:2750]
b1_fft_band7 = fft_band7.iloc[1950:2700]
#A1 Ads
a1_fft_band0 = fft_band0.iloc[23149:23276]
a1_fft_band1 = fft_band1.iloc[23149:23270]
a1_fft_band2 = fft_band2.iloc[23300:23470]
a1_fft_band3 = fft_band3.iloc[23300:23470]
a1_fft_band4 = fft_band4.iloc[22900:23000]
a1_fft_band5 = fft_band5.iloc[23400:23500]
a1_fft_band6 = fft_band6.iloc[23149:23300]
a1_fft_band7 = fft_band7.iloc[22980:23200]


# In[73]:


#B1
fig, ax = plt.subplots()
ax.set_xticklabels([])
plt.xlabel('Frequency')
plt.ylabel('FFT Band Value')
ax.set_xlim(0, 8000)

plt.plot(b1_fft_band0.index - 2000, b1_fft_band0['Value'], '.', markersize=5, label='Band 0')
plt.plot(b1_fft_band1.index - 1000, b1_fft_band1['Value'], '.', markersize=5, label='Band 1')
plt.plot(b1_fft_band2.index, b1_fft_band2['Value'], '.', markersize=5, label='Band 2')
plt.plot(b1_fft_band3.index + 1000, b1_fft_band3['Value'], '.', markersize=5, label='Band 3')
plt.plot(b1_fft_band4.index + 2000, b1_fft_band4['Value'], '.', markersize=5, label='Band 4')
plt.plot(b1_fft_band5.index + 3000, b1_fft_band5['Value'], '.', markersize=5, label='Band 5')
plt.plot(b1_fft_band6.index + 4000, b1_fft_band6['Value'], '.', markersize=5, label='Band 6')
plt.plot(b1_fft_band7.index + 5000, b1_fft_band7['Value'], '.', markersize=5, label='Band 7')

plt.title('Condition B1 Bands')
plt.legend(markerscale=3)

#A1
fig, ax = plt.subplots()
ax.set_ylim(0, 0.5)
ax.set_xticklabels([])
plt.xlabel('Frequency')
plt.ylabel('FFT Band Value')

plt.plot(a1_fft_band0.index - 2000, a1_fft_band0['Value'], '.', markersize=5, label='Band 0')
plt.plot(a1_fft_band1.index - 1000, a1_fft_band1['Value'], '.', markersize=5, label='Band 1')
plt.plot(a1_fft_band2.index, a1_fft_band2['Value'], '.', markersize=5, label='Band 2')
plt.plot(a1_fft_band3.index + 1000, a1_fft_band3['Value'], '.', markersize=5, label='Band 3')
plt.plot(a1_fft_band4.index + 2000, a1_fft_band4['Value'], '.', markersize=5, label='Band 4')
plt.plot(a1_fft_band5.index + 3000, a1_fft_band5['Value'], '.', markersize=5, label='Band 5')
plt.plot(a1_fft_band6.index + 4000, a1_fft_band6['Value'], '.', markersize=5, label='Band 6')
plt.plot(a1_fft_band7.index + 5000, a1_fft_band7['Value'], '.', markersize=5, label='Band 7')

plt.title('A1 Bands')
plt.legend(markerscale=3);


# # EO Bands Overall

# These bands show how different trials relate to each other
# Most of the action is seen surrounding Band 3, need to get what the frequency is

# In[79]:


def fftbands(temp, title):
    
    fig, (ax, ax2) = plt.subplots(1, 2, sharey=True)

    x = temp.index
    y = temp['Value']

    ax.set_ylabel('FFT Value', loc='center')

    ax2.tick_params(left = False, labelleft = False)


    # hide the spines between ax and ax2
    ax.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    #Set x and y axis limits
    ax.set_xticklabels([])
    ax2.set_xticklabels([])
    ax.set_xlim(0, 7500)
    ax2.set_xlim(22400, 28300)
    ax.set_ylim(0, 0.6)
    ax2.set_ylim(0, 0.6)

    d=0.025
    
    kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
    ax.plot((1-d,1+d), (-d,+d), **kwargs)
    ax.plot((1-d,1+d),(1-d,1+d), **kwargs)

    kwargs.update(transform=ax2.transAxes) 
    ax2.plot((-d,+d), (1-d,1+d), **kwargs)
    ax2.plot((-d,+d), (-d,+d), **kwargs)


    ax.axvspan(1958, 2720, color='pink', alpha=0.2, label='B1')
    ax.axvspan(3693, 4500, color='violet', alpha=0.2, label='B2')
    ax.axvspan(6643, 7403, color='mediumblue', alpha=0.2, label='B3')
    ax2.axvspan(23200, 23350, color='slategrey', alpha=0.2, label='A1')
    ax2.axvspan(23911, 24595, color='cyan', alpha=0.2, label='A2')
    ax2.axvspan(24669, 25187, color='lime', alpha=0.2, label='A3')
    ax2.axvspan(25496, 26114, color='yellow', alpha=0.2, label='A4')
    ax2.axvspan(26403, 26544, color='orange', alpha=0.2, label='A5')
    ax2.axvspan(26982, 27327, color='sienna', alpha=0.2, label='A6')
    ax2.axvspan(27510, 27826, color='red', alpha=0.2, label='A7')
    ax2.axvspan(27803, 28112, color='silver', alpha=0.2, label='A8')

    fig.suptitle(title)
    #fig.xlabel('Frequency')
    fig.legend(loc='upper right', bbox_to_anchor=(1,0.75), markerscale=3)
    fig.subplots_adjust(wspace=0.05)


    A = ax.plot(x, y, '.', color='black', markersize=3)
    B = ax2.plot(x, y, '.', color='black', markersize=3);
    
fftbands(fft_band0, 'Band 0')
fftbands(fft_band1, 'Band 1')
fftbands(fft_band2, 'Band 2')
fftbands(fft_band3, 'Band 3')
fftbands(fft_band4, 'Band 4')
fftbands(fft_band5, 'Band 5')
fftbands(fft_band6, 'Band 6')
fftbands(fft_band7, 'Band 7')

