# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:56:29 2020

@author: arb28
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig


lengthlist = [74.3,63.9,54.5,45.4,35.6]
periodlist = []
g = 9.81 #g in m/s^2



def updateSystem(cur_pos,cur_vel,cur_accel,cur_time):
    
    next_vel = cur_vel + cur_accel*dt
    next_pos = cur_pos + cur_vel*dt
    next_accel = -1*g/(length/100)*math.sin(next_pos) - 0.5*next_vel
    next_time = cur_time + dt
    
    return next_pos, next_vel, next_accel, next_time

def analysis(pos_arr):
    
    filtered_pos = sig.medfilt(pos_arr,5) #Filter the angular position
    
    
    shifted_ang_pos = filtered_pos - filtered_pos.mean()
    #Center the angular position about zero for analysis
    #The angular position centered around negatives values for some tests
    #so centering about zero will just shift the values and make the data
    #analysis better
    
    
    
    zero_array = np.array([]) #Create an empty array
    
    for i in range(len(shifted_ang_pos)-1): #Cycle through the angular poss
        
        if shifted_ang_pos[i] < 0 and shifted_ang_pos[i + 1] > 0:
        #If the angular pos changes from negative to positive that
        #represents a zero point
            zero_array = np.append(zero_array, i) #Save the index of 
                                                  #the negative value
    
    period_length_arr = np.array([])
    
  
    for i in range(len(zero_array)-1): #Cycle through the zero values
        
        first_zero_time = (time_arr[int(zero_array[i])] + 
                                            time_arr[int(zero_array[i]+1)])/2
        #Average the negative value and the positive value of the first peak
        
        second_zero_time = (time_arr[int(zero_array[i+1])] + 
                                             time_arr[int(zero_array[i+1]+1)])/2
        #Average the negative value and the positive value of the second peak
        
        period_length = second_zero_time - first_zero_time
        period_length_arr = np.append(period_length_arr, period_length)
        #Calculate the time between peaks and add it to the array
   
    average_period = period_length_arr.mean() #Find the mean period length
    
    
    print(average_period)
    
    periodlist.append(average_period) #Add the period length to the
                                      #period list array

for i in lengthlist:
    
    cur_pos = math.pi/12 #current position in radians
    cur_vel = 0 #current velocity in radians/s
    length = i #length in cm
    cur_time = 0 #current time in seconds
    dt = 10**-3 #dt in seconds

    cur_accel = -1*g/(length/100)*math.sin(cur_pos)
    
    pos_arr = np.array([cur_pos])
    vel_arr = np.array([cur_vel])
    accel_arr = np.array([cur_accel])
    time_arr = np.array([cur_time])
    

    
    while cur_time < 10:
        
       cur_pos,cur_vel,cur_accel,cur_time = updateSystem(cur_pos,
                                                         cur_vel,
                                                         cur_accel,
                                                         cur_time)
        
       pos_arr = np.append(pos_arr, cur_pos)
       vel_arr = np.append(vel_arr, cur_vel)
       accel_arr = np.append(accel_arr, cur_accel)
       time_arr = np.append(time_arr, cur_time)
        

    
    analysis(pos_arr)
        
        
    plt.plot(time_arr,pos_arr, label = "pos (rad)")
    plt.plot(time_arr,vel_arr, label = "vel (rad/s)")
    plt.plot(time_arr,accel_arr, label = "accel (rad/s^2)")
    plt.suptitle("Acceleration, Velocity, Position at " + str(i) + " cm")
    plt.xlabel("Time (s)")
    plt.legend()
    
    plt.show()

plt.figure(6) #Create a 6th graph (5x1 = 5)
plt.plot(lengthlist,periodlist) #Graph period vs length
plt.suptitle("Period vs Length") #Add titles, lables
plt.xlabel("Length (cm)")
plt.ylabel("Period (s)")