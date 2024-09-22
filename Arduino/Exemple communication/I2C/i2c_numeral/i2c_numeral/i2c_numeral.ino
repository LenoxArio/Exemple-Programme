#include <Wire.h>

const int ledPin = 13;

void setup(){
  Serial.begin(9600);
  Wire.begin(0x8);
  Wire.onReceive(receiveEvent);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

void loop(){
  delay(100);
}

void receiveEvent(int howMany){
  while(Wire.available()){
    char command = Wire.read();
    if(command == 0x12){
      Serial.println("Hello");
    }
  }
}