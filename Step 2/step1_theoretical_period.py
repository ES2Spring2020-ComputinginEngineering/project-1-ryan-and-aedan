import numpy as np
import matplotlib.pyplot as plt

#The theoretical equation used to find the period of a simple pendulum assumes
#that there is no friction or drag, the pendulum structure is perfectly rigid, 
#and the string holding the mass is massless and doesn't stretch. Also, the simple pendulum 
#equation only works for small angles of movement when sin theta is approximately equal to theta.

lengths = [74.3, 63.9,54.5,45.4,35.6] #measured in centimeter
arrlength = np.array(lengths)

def length_to_period(length_array):   
#Takes an array of pendulum lengths and returns an array of the periods 
#for those respective lengths with the pendulum equation
    return 2*np.pi*np.sqrt((length_array/100)/9.81)

arrperiod = length_to_period(arrlength)

def plotter(length_array,period_array):
#Plots length vs period using the length and period arrays   
    plt.plot(length_array,2*np.pi*np.sqrt(length_array/100)/9.81)
    plt.title("Theoretical Period vs Length") 
    plt.xlabel("Pendulum Length (cm)")
    plt.ylabel("Period Length (s)")
    plt.show()
    
plotter(arrlength,arrperiod)