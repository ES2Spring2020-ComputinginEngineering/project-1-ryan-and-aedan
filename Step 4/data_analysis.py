# -*- coding: utf-8 -*-


import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

#os.chdir(r"C:\Users\hanki\OneDrive\Documents\GitHub\hw1-ryan-hankins\project-1-ryan-and-aedan\Step 3")
os.chdir(r"C:\Users\arb28\Desktop\School\Freshman\ES 2\Homework\project-1-ryan-and-aedan\Step 3")

fin = open('74.3cm.csv','r') #Add file name

x_accel = np.array([])
y_accel = np.array([])
z_accel = np.array([])
time = np.array([])
time_initial = 0



for line in fin:
    t = line.strip().split(',')
    if t != ['']:
        x_accel = np.append(x_accel,float(t[0])/1000)
        y_accel = np.append(y_accel,float(t[1])/1000)
        z_accel = np.append(z_accel,float(t[2])/1000)
        time = np.append(time,float(t[3]))
        
time_initial = time[0]
for i in range(len(time)):
    time[i] = (time[i] - time_initial)/1000
    
    
angular_pos = np.arctan2(y_accel,z_accel)
    
fig, axes = plt.subplots(2, sharex=True)


axes[0].plot(time,y_accel)
axes[0].plot(time,z_accel)
axes[0].plot(time,x_accel)
axes[0].set_title("Accel")
axes[0].set(xlim=(0,60))
axes[1].plot(time,angular_pos)
axes[1].set_title("Ang Pos")
axes[1].set(xlim=(0,60))
fig.tight_layout()

filtered_ang_pos = sig.medfilt(angular_pos)

peak_array, _ = sig.find_peaks(filtered_ang_pos)

period_length_arr = np.array([])

for i in range(len(peak_array)-1):
    
    period_length_arr = np.append(period_length_arr, time[peak_array[i+1]] - time[peak_array[i]])

average_period = period_length_arr.mean()

print(average_period)
    


fin.close()