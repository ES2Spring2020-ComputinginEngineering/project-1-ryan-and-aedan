# -*- coding: utf-8 -*-

import csv
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\hanki\OneDrive\Documents\GitHub\hw1-ryan-hankins\project-1-ryan-and-aedan\Step 3")

fin = open('74.3cm.csv','r') #Add file name

x_accel = np.array([])
y_accel = np.array([])
z_accel = np.array([])
time = np.array([])



for line in fin:
    t = line.strip().split(',')
    if t != ['']:
        x_accel = np.append(x_accel,float(t[0]))
        y_accel = np.append(y_accel,float(t[1]))
        z_accel = np.append(z_accel,float(t[2]))
        time = np.append(time,float(t[3]))
    

    
