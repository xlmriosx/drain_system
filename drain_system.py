import board, time, digitalio, busio

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

def json_str(button, coil_in, sound_alert):
#     2022-26-11T13:59:59Z
    date = time.localtime()
    date = f'{date[0]}-{date[1]}-{date[2]}T{date[3]}:{date[4]}:{date[5]}Z'
    header = f'''"controller_name":"Raspberry-Pi-Pico", "date":"{date}",'''
    actuators_sound_alert = f'''"type":"buzzer", "current_state":"{sound_alert}"'''
    actuators_coil_in = f'''"type":"engine_drainer", "current_state":"{coil_in}"'''
    actuators = "[{"+actuators_sound_alert+"},"+"{"+actuators_coil_in+"}],"
    sensors_position_hg = f'''"type":"sensor_position_hg", "current_state":"{button}"'''
    sensors = "[{"+sensors_position_hg+"}]"
    json = "{\n"+header+'\n"actuators":'+actuators+'\n"sensors":'+sensors+"\n}"
    print(json)


while True:
    # To read all time what value have waters' sensor
    button.direction = digitalio.Direction.INPUT
    time.sleep(5)
    if button.value:
        button_js = "on"
        
        coil_in_js = "on"
        coil_in = True
        
        sound_alert_js = "on"
        sound_alert.value =True
        time.sleep(1)
        sound_alert.value = False
        time.sleep(1)
    
    if not button.value:
        button_js = "off"
        
        coil_in_js = "off"
        coil_in = False
        
        sound_alert_js = "off"
        
    json_str(button_js, coil_in_js, sound_alert_js)
#     print("No existe peligro de inundación.")