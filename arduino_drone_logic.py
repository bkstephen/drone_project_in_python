import time
#import gyro

import serial
 
def main():    
    #serial set up
    port = serial.Serial('/dev/ttyUSB0', 9600) # change name, if needed
    port.close()
    port.open()
    time.sleep(5)

    #the motor has 5 speeds (5, 6, 7, 8, 9)
    try:
        while True:
            s = input("Give thrust: ")
            p = input("Propeller (A/x/X/y/Y)")            
             
            # Send the code to be decoded p if the propeller, s is the speed, e determines the end of the data              
            port.write(str.encode(p))        
            port.write(str.encode(s))                  
            # port.write(str.encode("e"))             

    except KeyboardInterrupt:
        port.close()        

try:
    main()  #run main()
except:
    print("Something went wrong")
finally:
    main()

#TODO create communicaiton between the arduino and pi using serial9600 by decoding the data received