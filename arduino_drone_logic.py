import RPi.GPIO as GPIO
import time
import gyro
# pins for wing management 19, 9, 20, 8
# pins with 5v 26, 11, 25, 16

def main():
    # set up
    thrust = 19
    propeller = 9


    GPIO.setmode(GPIO.BCM)
    GPIO.setup(thrust, GPIO.OUT)
    GPIO.setup(propeller, GPIO.OUT)

    w1 = GPIO.PWM(wing1, 50) # GPIO 19 for PWM with 50Hz
    w2 = GPIO.PWM(wing2, 50)
    w3 = GPIO.PWM(wing3, 50)
    w4 = GPIO.PWM(wing4, 50)
    w1.start(0) # Initialization
    w2.start(0)
    w3.start(0)
    w4.start(0)
    w1.ChangeDutyCycle(0)
    w2.ChangeDutyCycle(0)
    w3.ChangeDutyCycle(0)
    w4.ChangeDutyCycle(0)


#the motor has 5 speeds (5, 6, 7, 8, 9)

    try:
        while True:

            s = input("Give thrust: ")            
            print(gyro.get_data())
            w1.ChangeDutyCycle(float(s))
            w2.ChangeDutyCycle(float(s))
            w3.ChangeDutyCycle(float(s))
            w4.ChangeDutyCycle(float(s))
            time.sleep(0.1)    
    except KeyboardInterrupt:
        w1.stop()
        w2.stop()
        w3.stop()
        w4.stop()
        GPIO.cleanup()

try:
    main()  #run main()
except:
    print("Something went wrong")
finally:
    main()