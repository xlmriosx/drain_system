#include <Wire.h>
#include <time.h>

const int sensor = 2;
const int coil = 4;
const int buzzer = 7;


void setup() {
  Wire.begin(4);                /* join i2c bus with address 4 */
  // Wire.onReceive(receiveEvent); /* register receive event */
  // Wire.onRequest(requestEvent); /* register request event */
  Serial.begin(9600);           /* start serial for debug */
  pinMode(sensor, INPUT);  // Sensor
  pinMode(coil, OUTPUT); // Coil
  pinMode(buzzer, OUTPUT); // Buzzer
  digitalWrite(sensor, HIGH);

}

void loop() {
  int sensor_json = 0;
  int coil_json = 1;
  int buzzer_json = 1;
  int sensor_state = digitalRead(sensor);
  if(sensor_state == 0){
    digitalWrite(coil, HIGH);
    
    digitalWrite(buzzer, HIGH);
    delay(500);
    digitalWrite(buzzer, LOW);
    delay(500);

    int sensor_json = 0;
    int coil_json = 1;
    int buzzer_json = 1;
  }
  if(sensor_state == 1){
    digitalWrite(coil, LOW);

    int sensor_json = 1;
    int coil_json = 0;
    int buzzer_json = 0;
  }
  write_serial_wire(buzzer_json, coil_json, sensor_json);
  Serial.println();
  
}

void write_serial_wire(int buzzer_json, int coil_json, int sensor_json){
  Serial.print("{\"controller_name\":\"Raspberry-Pi-Pico\",");
  Serial.print("\"date\":\"\",");
  Serial.print("\"actuators\":\[{\"type\":\"speaker\",\"current_value\":");
  Serial.print(buzzer_json);Serial.print("},");
  Serial.print("{\"type\":\"rele\",\"current_value\":");
  Serial.print(coil_json);Serial.print("}],");
  Serial.print("\"sensors\":[{\"type\":\"position_sensor\",\"current_value\":");
  Serial.print(coil_json);Serial.print("}]}");
  
  Wire.write("{\"controller_name\":\"Raspberry-Pi-Pico\",");
  Wire.write("\"date\":\"\",");
  Wire.write("\"actuators\":\[{\"type\":\"speaker\",\"current_value\":");
  Wire.write(buzzer_json);Wire.write("},");
  Wire.write("{\"type\":\"rele\",\"current_value\":");
  Wire.write(coil_json);Wire.write("}],");
  Wire.write("\"sensors\":[{\"type\":\"position_sensor\",\"current_value\":");
  Wire.write(coil_json);Wire.write("}]}");
}


// function that executes whenever data is received from master
void receiveEvent(int howMany) {
 while (0 < Wire.available()) {
    char c = Wire.read();      /* receive byte as a character */
    Serial.print(c);           /* print the character */
  }
  Serial.println();             /* to newline */
}

// function that executes whenever data is requested from master
void requestEvent() {
  

}
