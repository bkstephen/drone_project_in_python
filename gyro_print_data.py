
import smbus                    #import SMBus module of I2C
from time import sleep          #import

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19

CONFIG       = 0x2A

GYRO_CONFIG  = 0x1B

INT_ENABLE   = 0x2D

ACCEL_XOUT_H = 0x02
ACCEL_YOUT_H = 0x04
ACCEL_ZOUT_H = 0x06
GYRO_XOUT_H  = 0x01
GYRO_YOUT_H  = 0x03
GYRO_ZOUT_H  = 0x05

OFF_X = 0x2F
OFF_Y = 0x30
oFF_Z = 0x31

def MPU_Init():
        #write to sample rate register

#       bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

        #Write to power management register
#       bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

        #Set offsets for accuracy
#       bus.write_byte(OFF_X, 1)

        #Write to Configuration register
        n = bus.read_byte_data(Device_Address, CONFIG)
        bus.write_byte_data(Device_Address, CONFIG, n)
        bus.write_byte_data(Device_Address, CONFIG, 1)

        #Write to Gyro configuration register
        bus.write_byte_data(Device_Address, GYRO_CONFIG, 1)

        #Write to interrupt enable register
        bus.write_byte_data(Device_Address, INT_ENABLE, 1)


def read_raw_data(addr):
        #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | int(str(low)[:1]))

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value #1.96 is for adjustment purposes


bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x1C   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

# Variables that at the begining of readings take average offsets
# To work properly the sernsor must lie as flat as possible
adjustment_counter = 10
x_adjustment = 0
y_adjustment = 0
z_adjustment = 0

while True:

        #Read Accelerometer raw value
        acc_x = read_raw_data(ACCEL_XOUT_H)
        acc_y = read_raw_data(ACCEL_YOUT_H)
        acc_z = read_raw_data(ACCEL_ZOUT_H)

        #Read Gyroscope raw value
        gyro_x = read_raw_data(GYRO_XOUT_H)
        gyro_y = read_raw_data(GYRO_YOUT_H)
        gyro_z = read_raw_data(GYRO_ZOUT_H)

        #Full scale range +/- 250 degree/C as per sensitivity scale factor
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0

        Gx = gyro_x/131.0 - x_adjustment
        Gy = gyro_y/131.0 - y_adjustment
        Gz = gyro_z/131.0 - z_adjustment

        if(adjustment_counter <= 10 and adjustment_counter > 0):
            x_adjustment = gyro_x/131.0 + x_adjustment
            y_adjustment = gyro_y/131.0 + y_adjustment
            z_adjustment = gyro_z/131.0 + z_adjustment
            adjustment_counter-=1
        elif(adjustment_counter==0):
            x_adjustment = x_adjustment/10
            y_adjustment = y_adjustment/10
            z_adjustment = z_adjustment/10
            adjustment_counter-=1




        #print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)
        sleep(0.1)

        print ("Gx=%.2f" %Gx, " \tGy=%.2f" %Gy," \tGz=%.2f" %Gz," \tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az)
