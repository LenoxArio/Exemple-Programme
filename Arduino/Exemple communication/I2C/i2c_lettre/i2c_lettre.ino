#include <Wire.h>

String receivedMessage = "";

void setup() {
  Serial.begin(9600);
  Wire.begin(0x8);
  Wire.onReceive(receiveEvent);
}

void loop() {
  delay(100);
}

void receiveEvent(int howMany) {
  while (Wire.available()) {
    char command = Wire.read();
    receivedMessage += command;  // Concaténer chaque caractère reçu

    Serial.println(command);
  }
  if (receivedMessage == "hello") { // Vérifier si le message complet est "hello"
    Serial.println("Received: hello");
    receivedMessage = "";  // Réinitialiser la variable pour recevoir un nouveau message
  }
}
