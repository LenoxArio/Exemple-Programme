#include <Wire.h>

const int ledPin = 13;
static_assert(LOW == 0, "Expecting LOW to be 0");

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
    char c = Wire.read();
    digitalWrite(ledPin, c);
  }
}