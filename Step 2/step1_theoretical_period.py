import numpy as np
import matplotlib.pyplot as plt


lengths = [74.3, 63.9,54.5,45.4,35.6] #measured in centimeter
arrlength = np.array(lengths)

def length_to_period(length_array):
    plt.plot(length_array,2*np.pi*np.sqrt((length_array/100)/9.81))
    plt.show()
    return 2*np.pi*np.sqrt((length_array/100)/9.81)

arrperiod = length_to_period(arrlength)