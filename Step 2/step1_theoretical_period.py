import numpy as np
import matplotlib.pyplot as plt

#Still need to write a comment explaining the real world limit of model

lengths = [74.3, 63.9,54.5,45.4,35.6] #measured in centimeter
arrlength = np.array(lengths)

def length_to_period(length_array):

    return 2*np.pi*np.sqrt((length_array/100)/9.81)

arrperiod = length_to_period(arrlength)

def plotter(length_array,period_array):
    plt.plot(length_array,2*np.pi*np.sqrt((length_array/100)/9.81))
    plt.title("Title") ##Add title
    plt.xlabel("Pendulum Length (cm)")
    plt.ylabel("Period Length (s)")
    plt.show()
    
plotter(arrlength,arrperiod)