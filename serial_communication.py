import time
import serial
 
def main():       

    while True:
        #the motor has 5 speeds (5, 6, 7, 8, 9)
        s = input("Give thrust: ")
        p = input("Propeller (A/x/X/y/Y)")            
        send_data(s, p, '/dev/ttyUSB0');
        # Send the code to be decoded p if the propeller, s is the speed, e determines the end of the data              
                           
  

def send_data(s , p, serialLocationString):
    try:
        #serial set up
        port = serial.Serial(serialLocationString, 9600) # change USB, if needed
        port.close()
        port.open()        
        time.sleep(5)
        port.write(str.encode(p))        
        port.write(str.encode(s))  
    except KeyboardInterrupt:        
        port.close()   

try:
    main()  #run main()
except:
    print("Something went wrong")
finally:
    main()