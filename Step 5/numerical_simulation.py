# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:56:29 2020

@author: arb28
"""

import math
import numpy as np
import matplotlib.pyplot as plt

current_time = 0
dt = 10**-2
current_position = math.pi/4
current_velocity = 0
length = 1
g = 9.81
current_acceleration = -1*g/length*math.sin(current_position)

pos_arr = np.array([current_position])
vel_arr = np.array([current_velocity])
accel_arr = np.array([current_acceleration])
time_arr = np.array([current_time])



print("Position",current_position)
print("Velocity",current_velocity)
print("Acceleration",current_acceleration)

while current_time < 20:
    
    next_velocity = current_velocity + current_acceleration*dt
    next_position = current_position + current_velocity*dt
    next_acceleration = -1*g/length*math.sin(next_position) - 0.7*current_velocity
    next_time = current_time + dt
    
    current_position = next_position
    current_velocity = next_velocity
    current_acceleration = next_acceleration
    current_time = next_time
    
    print("Position",next_position)
    print("Velocity",next_velocity)
    print("Acceleration",next_acceleration)
    print("Time",next_time)
    print("\n")
    

    pos_arr = np.append(pos_arr, current_position)
    vel_arr = np.append(vel_arr, current_velocity)
    accel_arr = np.append(accel_arr, current_acceleration)
    time_arr = np.append(time_arr, current_time)
    
plt.plot(time_arr,pos_arr)
plt.show()
    