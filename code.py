from machine import Pin, ADC
import time
import json

# To make sure microcontroller is working
led = Pin("LED", Pin.OUT)
led.off()

# Reference to sensor water
sensor_position = Pin(16, Pin.IN, Pin.PULL_UP)

# Energy coil to activate engine
coil_in = Pin(0, Pin.OUT, Pin.PULL_DOWN)
coil_in.off()

# Alarm
sound_alert = Pin(1, Pin.OUT, Pin.PULL_DOWN)
sound_alert.off()

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
    return json

while True:
    print(sensor_position.value())
    led.on()
    coil_in.on()
    time.sleep_ms(500)
    led.off()
    
    
    if (sensor_position.value()):
        button_js = "on"
        
        coil_in_js = "on"
        coil_in.on()
        
        sound_alert_js = "on"
        sound_alert.on()
        time.sleep(1.5)
        sound_alert.off()
        time.sleep(1.5)
    
    if (not sensor_position.value()):
        button_js = "off"
        
        coil_in_js = "off"
        coil_in.off()
        
        sound_alert_js = "off"
        time.sleep(3)
    
    json_data = json_str(button_js, coil_in_js, sound_alert_js)
    print(json_str(button_js, coil_in_js, sound_alert_js))
     #     print("No existe peligro de inundación.")
    serialized_data = json.dumps(json_data)
   
