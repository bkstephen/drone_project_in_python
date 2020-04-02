import time
#import gyro

import serial
import serial_communication
 
def main():    

    while True:
        s = input("Give thrust: ")
        p = input("Propeller (A/x/X/y/Y)")     
        serial_communication.write(s, p)       
    
main()

#TODO create communicaiton between the arduino and pi using serial9600 by decoding the data received