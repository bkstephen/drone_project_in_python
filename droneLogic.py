import RPi.GPIO as GPIO
import time

# pins for wing management 19, 9, 20, 8
# pins with 5v 26, 11, 25, 16

def main():
    # set up
    wing1 = 19
    wing2 = 9
    wing3 = 20
    wing4 = 8

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(wing1, GPIO.OUT)
    GPIO.setup(wing2, GPIO.OUT)
    GPIO.setup(wing3, GPIO.OUT)
    GPIO.setup(wing4, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(25, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)

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
            w1.ChangeDutyCycle(s)
            w2.ChangeDutyCycle(s)
            w3.ChangeDutyCycle(s)
            w4.ChangeDutyCycle(s)
            time.sleep(0.5)
    except KeyboardInterrupt:
        w1.stop()
        w2.stop()
        w3.stop()
        w4.stop()
        GPIO.cleanup()

main()  #run main()