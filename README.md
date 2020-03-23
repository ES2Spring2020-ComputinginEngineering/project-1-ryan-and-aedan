## Project 1
Project 1 - Micro:bit Pendulum

Names: Ryan Hankins and Aedan Brown
Team Name: Ryan and Aedan

This project involved analysis of pendulum movement in three different parts: one based on recorded data, one based on simulation, 
and one based on theoretical physics. Using two microbits, one as a transmitter and the other as a receiver, the accelerometer data of a 
swinging pendulum was logged and used to create graphs for acceleration, velocity, and position versus time as well as period versus the 
length of the pendulum. Graphs were also made by using the simple pendulum equation at different lengths and theoretical physics to simulate 
how a pendulum should move.

## Instructions

step1_theortical_period.py - Clicking the run button will produce the theoretical period vs. length graph

logger.py/receiver.py - These files contain comments about how to use logger and reciever

data_analysis.py - First, os.chdir() has to be used to change the directory to the Step 3 folder in the project file. This folder contains all 
the real-world data logs that will be used in the analysis code. There is already a os.chdir() line at the beginning of the code. Once it 
is changed, running the code will print the 5 periods along with the acceleration versus time and angular position versus time for the different 
pendulum lengths.

numerical_simulation.py - Running the script will, for all 5 pendulum lengths, print the period based on the simulation and create a graph of 
angular acceleration, velocity, and position versus time. At the end it will produce of graph of periods versus pendulum lengths.
