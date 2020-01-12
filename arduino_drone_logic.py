import RPi.GPIO as GPIO
import time
import gyro

import serial
 
def main():
    # set up
    #serial set up
    s = serial.Serial('/dev/ttyUSB0', 9600) # change name, if needed
    s.close()
    s.open()
    time.sleep(5)

    #the motor has 5 speeds (5, 6, 7, 8, 9)
    try:
        while True:
            
            response = s.readline()
            print(response) 

            s = str(input("Give thrust: "))
            s = "test"            
            print(gyro.get_data())
                        
            s.write(s.encode())            
            time.sleep(0.3)              

    except KeyboardInterrupt:
        s.close()
        GPIO.cleanup()

try:
    main()  #run main()
except:
    print("Something went wrong")
finally:
    main()