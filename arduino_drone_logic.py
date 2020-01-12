import RPi.GPIO as GPIO
import time
import gyro

import serial
 
s = serial.Serial('/dev/ttyAMA0', 9600) # change name, if needed
s.close()
s.open()
time.sleep(5) # the Arduino is reset after enabling the serial connection, therefore we have to wait some seconds
 
s.write({!r}'.format("test"))
try:
    while True:
        response = s.readline()
        print(response)
except KeyboardInterrupt:
    s.close()

def main():
    # set up
    thrust = 16 #white -> 7
    propeller = 20 #red -> 6

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(thrust, GPIO.OUT)
    GPIO.setup(propeller, GPIO.OUT)

    w1 = GPIO.PWM(propeller, 100) # GPIO 19 for PWM with 50Hz
    w2 = GPIO.PWM(thrust, 100)
    w1.start(0) # Initialization
    w2.start(0)
    w1.ChangeDutyCycle(float(0))
    w2.ChangeDutyCycle(float(0))


#the motor has 5 speeds (5, 6, 7, 8, 9)

    try:
        while True:
            s = input("Give thrust: ")            
            print(gyro.get_data())
            w1.ChangeDutyCycle(float(0))
            w2.ChangeDutyCycle(float(s))
            time.sleep(0.3)    
            w1.ChangeDutyCycle(float(6))            
    except KeyboardInterrupt:
        w1.stop()
        w2.stop()
        GPIO.cleanup()

try:
    main()  #run main()
except:
    print("Something went wrong")
finally:
    main()