import board
import time
import digitalio
 
# Reference to sensor water
button = digitalio.DigitalInOut(board.GP3)
# button.direction = digitalio.Direction.INPUT
 
# Energy coil to activate engine
coil_in = digitalio.DigitalInOut(board.GP13)
coil_in.direction = digitalio.Direction.OUTPUT
 
# Reference to energy network to connect filter engine
energy_engine = digitalio.DigitalInOut(board.GP15)
energy_engine.direction = digitalio.Direction.OUTPUT
energy_engine.value = True
 
# To make sure microcontroller is working
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
 
# Alarm
sound_alert = digitalio.DigitalInOut(board.GP17)
sound_alert.direction = digitalio.Direction.OUTPUT
 
while True:
    # To read all time what value have waters' sensor
    button.direction = digitalio.Direction.INPUT
    while not button.value:
        if button.value:
            coil_in = True
        led.value = True
        sound_alert.value =True
        time.sleep(1)
        ###
        led.value = False
        sound_alert.value = False
        time.sleep(1)
        print(button.value)
    time.sleep(2)
    coil_in = False
    print(button.value)
