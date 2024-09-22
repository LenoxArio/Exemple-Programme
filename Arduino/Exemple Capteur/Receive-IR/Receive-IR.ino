/*
code de : https://github.com/Arduino-IRremote/Arduino-IRremote

le recepteur doit être connecter sur la broche 2 de l'arduino   (pin Y = 2)

*/

#include <IRremote.hpp>
#define IR_RECEIVE_PIN 2

void setup()
{
  Serial.begin(115200); // // Establish serial communication
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK); // Start the receiver
}

void loop() {
  if (IrReceiver.decode()) {
      Serial.println(IrReceiver.decodedIRData.decodedRawData, HEX); // Print "old" raw data
      IrReceiver.printIRResultShort(&Serial); // Print complete received data in one line
      IrReceiver.printIRSendUsage(&Serial);   // Print the statement required to send this data
    
      IrReceiver.resume(); // Enable receiving of the next value
  }

}