# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt



fin = open('') #Add file name

x_accel = np.array()
y_accel = np.array()
z_accel = np.array()
time = np.array()



for line in fin:
    t = line.split(',')
    x_accel.append(t[0])
    y_accel.append(t[1])
    z_accel.append(t[2])
    time.append(t[3])
    

    
