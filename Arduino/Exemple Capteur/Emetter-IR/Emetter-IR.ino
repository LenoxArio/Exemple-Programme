/*
 *
 *  This file is part of Arduino-IRremote https://github.com/Arduino-IRremote/Arduino-IRremote.

########################Partie Fr########################
 Code pour envoyer un signal IR
 l'emeteur doit être connecter sur la broche 2 de l'arduino
 Pour envoyer vous devez entré l'adresse, la commande et le Data
 */
#include <Arduino.h>

#if !defined(ARDUINO_ESP32C3_DEV) // This is due to a bug in RISC-V compiler, which requires unused function sections :-(.
#define DISABLE_CODE_FOR_RECEIVER // Disables static receiver code like receive timer ISR handler and static IRReceiver and irparams data. Saves 450 bytes program memory and 269 bytes RAM if receiving functions are not required.
#endif


#include <IRremote.hpp> // include the library
#define IR_SEND_PIN 2 //Pin de l'emeteur 


void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(115200);
    while (!Serial);
    Serial.println(F("START " __FILE__ " from " __DATE__ "\r\nUsing library version " VERSION_IRREMOTE));
    Serial.print(F("Send IR signals at pin "));
    Serial.println(IR_SEND_PIN);

    IrSender.begin(IR_SEND_PIN); // Start with IR_SEND_PIN -which is defined in PinDefinitionsAndMore.h- as send pin and enable feedback LED at default feedback LED pin
    disableLEDFeedback(); // Disable feedback LED at default feedback LED pin
}


void loop() {

    IrSender.sendNEC(0xDF00, 0x1C, 0xE31CDF00);  //envoyer un signal IR qui pour : adresse = 0xDF00  ;  commande = 0x1C  ;  Data = E31CDF00
    delay(1000);  // delay must be greater than 5 ms (RECORD_GAP_MICROS), otherwise the receiver sees it as one long signal
}
