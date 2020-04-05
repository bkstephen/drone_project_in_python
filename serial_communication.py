import time
import serial
 
def write(s, p):       
    try:
        #serial set up
        port = serial.Serial('/dev/ttyUSB0', 9600) # change USB, if needed
        port.close()
        port.open()        
        time.sleep(1)

        while True:
            #the motor has 5 speeds (5, 6, 7, 8, 9)         
            send_data(s, p, port);
            # Send the code to be decoded p if the propeller, s is the speed, e determines the end of the data 
         
    except KeyboardInterrupt:        
        port.close()        
    
def send_data(s , p, port):
        port.write(str.encode(p))        
        port.write(str.encode(s))  
    