#include <Wire.h>
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

}

void loop() {
  char cadena_json = "{}"
  int sensor_state = digitalRead(sensor);
  if(sensor_state == 1){
    digitalWrite(coil, HIGH);
    
    digitalWrite(buzzer, HIGH);
    delay(500);
    digitalWrite(buzzer, LOW);
    delay(500);

    char sensor_json = "on";
    char coil_json = "on";
    char buzzer_json = "on";
  }
  if(sensor_state == 0){
    digitalWrite(coil, LOW);

    char sensor_json = "off";
    char coil_json = "off";
    char buzzer_json = "off";
  }

  
}

// function that executes whenever data is received from master
void receiveEvent(int howMany) {
 while (0 < Wire.available()) {
    char c = Wire.read();      /* receive byte as a character */
    Serial.print(c);           /* print the character */
    Wire.write("asd");
  }
  Serial.println();             /* to newline */
}

// function that executes whenever data is requested from master
void requestEvent() {
  Serial.println();             /* to newline */
  Wire.write(Wire.read());  /*send string on request */

}

