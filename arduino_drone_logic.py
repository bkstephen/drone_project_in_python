import time
#import gyro

import serial
import serial_communication

def main():    


    while True:
        s = input("Give thrust: ")
        p = input("Propeller (A/x/X/y/Y)")     
        serial_communication.write(s, p)       

try:
    main()  #run main()
except:
    print("Something went wrong")
finally:
    main()



