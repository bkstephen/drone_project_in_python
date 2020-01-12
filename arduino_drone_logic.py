import RPi.GPIO as GPIO
import time
#import gyro

import serial
 
port = serial.Serial('/dev/ttyUSB0', 9600) # change name, if needed
port.close()
port.open()
time.sleep(5) # the Arduino is reset after enabling the serial connection, therefore we have to wait some seconds

def main():
    # set up
    #serial set up
    port = serial.Serial('/dev/ttyUSB1', 9600) # change name, if needed
    port.close()
    port.open()
    time.sleep(5)

    #the motor has 5 speeds (5, 6, 7, 8, 9)
    try:
        while True:
            s = input("Give thrust: ")
            #print(gyro.get_data())             
            st  = "test"               
            port.write(str.encode(st))     
                               
            
            response = port.readline()
            print(response) 


    except KeyboardInterrupt:
        port.close()
        GPIO.cleanup()

try:
    main()  #run main()
except:
    print("Something went wrong")
finally:
    main()