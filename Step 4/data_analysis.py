# PROJECT 1 --- ES2
# Pendulum Data Analysis

# FILL THESE COMMENTS IN
#*****************************************
# NAMES: Ryan Hankins and Aedan Brown
# NUMBER OF HOURS TO COMPLETE: 7
# YOUR COLLABORATION STATEMENT(s): We worked alone on this assignment
#
#
#*****************************************

import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

#os.chdir(r"C:\Users\hanki\OneDrive\Documents\GitHub\hw1-ryan-hankins\project-1-ryan-and-aedan\Step 3")
#os.chdir(r"C:\Users\arb28\Desktop\School\Freshman\ES 2\Homework\project-1-ryan-and-aedan\Step 3")

length_list = [74.3,63.9,54.5,45.4,35.6]
period_list = []

#FUNCTIONS---------------------------------------------------------------------
  

def fileprep(length):
    
    #fileprep parses the files so that the data can be used
    #The function takes one argument
        #length is the length of the pendulum which corresponds to the file name
    #The function returns the opened file, an array of the X-acceleration,
    #Y-acceleration, Z-acceleration, and time
    
    fin = open(str(length) + '.csv','r') #Open corresponding data file

    x_acc = np.array([]) #Create arrays for X, Y, Z accelerations and time
    y_acc = np.array([]) #These arrays are in the scope of the function
    z_acc = np.array([]) #and will be returned
    time = np.array([])
    
    
    for line in fin: #Parse the file
        t = line.strip().split(',') #Convert the string to a list
        if t != ['']: #The csv files contains empty lines that should be skipped
           
            #Add the accelerations in m/s^2 and time in ms
            x_acc = np.append(x_acc,float(t[0])*9.81/1000) 
            y_acc = np.append(y_acc,float(t[1])*9.81/1000)
            z_acc = np.append(z_acc,float(t[2])*9.81/1000)
            time = np.append(time,float(t[3]))
            
    time_initial = time[0] #Set the initial time to the first time value
    
    for i in range(len(time)): #Cycle through the time array and 
                               #subtract the initial time from each value
        time[i] = (time[i] - time_initial)/1000 #Convert to seconds as well

    return fin, x_acc, y_acc, z_acc, time



def analysis(ang_pos):
    
    #analysis analyzes the angular position to determine the peaks
    #The function takes in 1 argument
        #pos_arr is a array of the angular positions
    #The function does not return any values
        
    filtered_ang_pos = sig.medfilt(ang_pos,5) #Filter the angular position
    

    shifted_ang_pos = filtered_ang_pos - filtered_ang_pos.mean()
    #Center the angular position about zero for analysis
    #The angular position centered around negatives values for some tests
    #so centering about zero will just shift the values and make the data
    #analysis better
    
    zero_array = np.array([]) #Create an empty array
    
    for i in range(len(shifted_ang_pos)-1): #Cycle through the angular positions
        
        if shifted_ang_pos[i] < 0 and shifted_ang_pos[i + 1] > 0:
        #If the angular position changes from negative to positive that
        #represents a zero point
            zero_array = np.append(zero_array, i) #Save the index of 
                                                  #the negative value
    
    period_length_arr = np.array([])
    
  
    for i in range(len(zero_array)-1): #Cycle through the zero values
        
        first_zero_time = (time[int(zero_array[i])] + 
                                            time[int(zero_array[i]+1)])/2
        #Average the negative value and the positive value of the first peak
        
        second_zero_time = (time[int(zero_array[i+1])] + 
                                             time[int(zero_array[i+1]+1)])/2
        #Average the negative value and the positive value of the second peak
        
        period = second_zero_time - first_zero_time
        period_length_arr = np.append(period_length_arr, period)
        #Calculat the time between peaks and add it to the array
   
    average_period = period_length_arr.mean() #Find the mean period length
    
    
    print(average_period)
    
    period_list.append(average_period) #Add the period length to the
                                      #period list array


def plot(time,x_accel,y_accel,z_accel,angular_pos,length):
    
    #plot creates plots of the acceraltion and angular positions
    #It takes 6 arguments
        #time is an array of time values
        #x_accel is an array of x-acceleration values
        #y_accel is an array of y-acceleration values
        #z_accel is an array of z-acceleration values
        #angular_pos is an array of angular position values
        #length is the length of the pendulum that the data is associated with
    #The function has no return value
    
    fig, axes = plt.subplots(2, sharex=True, figsize=[10,8]) #Create figure 
                                                              #with subplots
    
    axes[0].plot(time,y_accel,label = "Y Accel") #Plot accelerations, 
                                                 #add titles and labels
    axes[0].plot(time,z_accel, label = "Z Accel")
    axes[0].plot(time,x_accel, label = "X Accel")
    axes[0].set_title("Acceleration vs Time (" + str(length) + " cm)")
    axes[0].set(xlabel="Time (s)",ylabel="Acceleration (m/s^2)")
    axes[0].set(xlim=(2.5,60))
    axes[0].legend(loc='upper right')
    
    axes[1].plot(time,angular_pos) #Plot angular positions, add titles and labels
    axes[1].set_title("Angular Position vs Time (" + str(length) + " cm)")
    axes[1].set(xlabel="Time (s)",ylabel="Angular Position (radians)")
    axes[1].set(xlim=(2.5,60))
    
    axes[0].label_outer() #Put the labels only on the outer edges
    axes[1].label_outer()
    fig.tight_layout() #Make the organization of the graph better



#MAIN--------------------------------------------------------------------------


for i in length_list: #Cycle through each length
    
    fin, x_accel, y_accel, z_accel, time = fileprep(i) #Assign return values to
                                                       #pass the value into
                                                       #other functions

    angular_pos = np.arctan(z_accel/y_accel) #Calculate the angular position
 
    analysis(angular_pos)
    
    plot(time,x_accel,y_accel,z_accel,angular_pos,i)

    
    fin.close() #Close the file

plt.figure(11) #Create a 11th graph (5x2 = 10)
plt.plot(length_list,period_list) #Graph period vs length
plt.suptitle("Period vs Length (Data)") #Add titles, lables
plt.xlabel("Length (cm)")
plt.ylabel("Period (s)")