##################
# Ryan Hankins and Aedan Brown
#Project1 Part 3 Receiver Code
#Time to Complete: 1 hour
#################

import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=20, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)

# Wait for start message before beginning printing

incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')

while True:
    incoming = radio.receive() # Read from radio
    #Takes incoming string from logger and plots it by using ',' as a delimiter
    #and turning the string into a tuple with 4 items
    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        #############################################################
        # FILL IN HERE
        # Incoming is string sent from logger
        # Need to parse it and reformat as a tuple for the MU plotter
        #############################################################
        info = tuple(int(data) for data in incoming.split(','))
        print(info)
        mb.sleep(10)