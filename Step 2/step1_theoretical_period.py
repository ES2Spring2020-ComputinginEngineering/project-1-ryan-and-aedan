import numpy as np
import matplotlib as plt


lengths = [74.3, 63.9,54.5,45.4,35.6] #measured in centimeter
arrlength = np.array(lengths)

def length_to_period(length_array):
    return 2*np.pi*np.sqrt((length_array/100)/9.81)

arrperiod = length_to_period(arrlength)