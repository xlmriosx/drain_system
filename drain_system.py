import board
import time
import digitalio
 
# Reference to sensor water
button = digitalio.DigitalInOut(board.GP3)
# button.direction = digitalio.Direction.INPUT
 
# Energy coil to activate engine
coil_in = digitalio.DigitalInOut(board.GP13)
coil_in.direction = digitalio.Direction.OUTPUT
 
# To make sure microcontroller is working
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
 
# Alarm
sound_alert = digitalio.DigitalInOut(board.GP17)
sound_alert.direction = digitalio.Direction.OUTPUT
 
while True:
    # To read all time what value have waters' sensor
    button.direction = digitalio.Direction.INPUT
    while not button.value:
        print("Existe peligro de inundación.")
        if button.value:
            coil_in = True
            print("Se activa el motor de filtrado.")
        print("Se activa la alarma.")
        sound_alert.value =True
        time.sleep(1)
        sound_alert.value = False
        time.sleep(1)
    time.sleep(2)
    coil_in = False
    print("No existe peligro de inundación.")
    
