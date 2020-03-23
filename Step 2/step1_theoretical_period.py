# PROJECT 1 --- ES2
# Theoretical Pendulum Periods

# FILL THESE COMMENTS IN
#*****************************************
# NAMES: Ryan Hankins and Aedan Brown
# NUMBER OF HOURS TO COMPLETE: 0.5
# YOUR COLLABORATION STATEMENT(s): We worked alone on this assignment
#
#
#*****************************************

import numpy as np
import matplotlib.pyplot as plt

#The theoretical equation used to find the period of a simple pendulum assumes
#that there is no friction or drag, the pendulum structure is perfectly rigid, 
#and the string holding the mass is massless and doesn't stretch. Also, the simple pendulum 
#equation only works for small angles of movement when sin theta is approximately equal to theta.

 
#FUNCTIONS---------------------------------------------------------------------

def length_to_period(length_array):   
#Takes an array of pendulum lengths and returns an array of the periods 
#for those respective lengths by using the pendulum equation
    return 2*np.pi*np.sqrt((length_array/100)/9.81)



def plotter(length_array,period_array):
#Plots length vs period using the length and period arrays. Has no return value   
    plt.plot(length_array,period_array)
    plt.title("Period vs Length (Theoretical)") 
    plt.xlabel("Pendulum Length (cm)")
    plt.ylabel("Period Length (s)")
    plt.show()

#MAIN--------------------------------------------------------------------------


lengths = np.array([74.3, 63.9,54.5,45.4,35.6]) #measured in centimeter
periods = length_to_period(lengths)
plotter(lengths,periods)