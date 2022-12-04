#Code for Raspberry Pi Pico
import utime
import machine
from machine import I2C,Pin
import uasyncio

led = machine.Pin(25, machine.Pin.OUT)
led.value(0)

I2C_Arduino = 0x04 #I2C Address of NodeMCU
data = "Nada" #Data to send to I2C device

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=10000)
print(i2c)
print("Initalizing I2C as Master")


### CONFIG Sensor water ###
sensor_position = Pin(16, Pin.IN, Pin.PULL_DOWN)
###########################

### CONFIG Energy coil to activate engine ###
coil_in = Pin(15, Pin.OUT)
coil_in.off()
######################################

### CONFIG Alarm ###
sound_alert = Pin(13, Pin.OUT)
sound_alert.off()
####################

def json_str(sensor, coil, buzzer):
#   2022-26-11T13:59:59Z
    return 'header '
    
    

while True:
    if (sensor_position.value()):
        coil_in.on()
        sound_alert.on()
        utime.sleep(1)
        sound_alert.off()
        utime.sleep(1)
        buzzer = 1
        
    else:
        coil_in.off()
        buzzer = 0
        
    try:
        print(json_str(sensor_position.value(), coil_in.value(),buzzer))
        data = '4-S1:'+str(sensor_position.value())+'-A1:'+str(coil_in.value())+'-A2:'+str(buzzer)
        message = 'Sending: ['+data+'] to: I2C_Arduino'
        print(message)
        i2c.writeto(I2C_Arduino, data) #This line is responsible for sending data to nodemcu 
        a = i2c.readfrom(I2C_Arduino,6) #This line responsible for read data from Nodemcu
        led.value(1)
        print(a)
        utime.sleep(0.1)
        led.value(0)
        utime.sleep(0.1)
    except:
        print('Error de conexion')
        
