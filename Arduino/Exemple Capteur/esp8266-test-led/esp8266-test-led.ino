/*
########CODE DEFAILLANT########
! Le code fonctionne mal avec nos test mais peu comme même fonctionner !


Lien de la page: https://www.robotique.site/tutoriel/allumer-deux-leds-connectees-a-larduino-uno-via-wifi/


La LED rouge devrait s’allumer en réponse à la requête suivante (http://192.168.1.48/?led=1).

La LED rouge devrait s’éteindre en réponse à la requête suivante (http://192.168.1.48/?led=0).

La LED verte devrait s’allumer en réponse à la requête suivante (http://192.168.1.48/?led=3).

La LED verte devrait s’éteindre en réponse à la requête suivante (http://192.168.1.48/?led=2).

*/


#include <SoftwareSerial.h>

SoftwareSerial esp8266(2, 3); // Pin 2 & 3 of Arduino as RX and TX. Connect TX and RX of ESP8266 respectively.
#define DEBUG true
#define red_led_pin 4          // Red LED is connected to Pin 4 of Arduino
#define green_led_pin 5        // Green LED is connected to Pin 5 of Arduino

void setup() {
  pinMode(red_led_pin, OUTPUT);
  digitalWrite(red_led_pin, LOW);
  pinMode(green_led_pin, OUTPUT);
  digitalWrite(green_led_pin, LOW);
  Serial.begin(9600);
  esp8266.begin(115200); // Baud rate for communicating with ESP8266. Yours might be different.
  esp8266Serial("AT+RST\r\n", 5000, DEBUG);         // Reset the ESP8266
  esp8266Serial("AT+CWMODE=1\r\n", 5000, DEBUG);    // Set station mode Operation
  esp8266Serial("AT+CWJAP=\"Livebox-3E91\",\"DtfcVx43NzvZh6L5Hv\"\r\n", 5000, DEBUG);
  Serial.println("Le serveur est Connecter !");
  esp8266Serial("AT+CIFSR\r\n", 5000, DEBUG);      // You will get the IP Address of the ESP8266 from this command.
  esp8266Serial("AT+CIPMUX=1\r\n", 5000, DEBUG);
  esp8266Serial("AT+CIPSERVER=1,80\r\n", 5000, DEBUG);
}

void loop() {
  if (esp8266.available()) {
    if (esp8266.find("+IPD,")) {
      String msg;
      esp8266.find("?");
      msg = esp8266.readStringUntil(' ');
      String command1 = msg.substring(0, 3);
      String command2 = msg.substring(4);

      if (DEBUG) {
        Serial.println(command1); // Must print "led"
        Serial.println(command2); // Must print "O" , "1"  , "2"  ou "3"
      }
      delay(100);

      if (command2 == "0") {
        digitalWrite(red_led_pin, LOW); // Eteindre la LED rouge
      }

      if (command2 == "1") {
        digitalWrite(red_led_pin, HIGH); // Allumer la LED rouge
      }

      if (command2 == "2") {
        digitalWrite(green_led_pin, LOW); // Eteindre la LED verte
      }

      if (command2 == "3") {
        digitalWrite(green_led_pin, HIGH); // Allumer la LED verte
      }
   
    }
  }
}

String esp8266Serial(String command, const int timeout, boolean debug) {
  String response = "";
  esp8266.print(command);
  long int time = millis();
  while ((time + timeout) > millis()) {
    while (esp8266.available()) {
      char c = esp8266.read();
      response += c;
    }
  }
  if (debug) {
    Serial.print(response);
  }
  return response;
}
