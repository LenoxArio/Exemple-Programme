/*
Version français:
installer la lib: DFRobotDFPlayerMini
lien vers le cablage : https://arduino.stackexchange.com/questions/89355/mp3-tf-16p-only-works-while-connected-to-serial-monitor
Le vert = RX
Le jaune = TX

*/

#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"
SoftwareSerial mySoftwareSerial(10, 11); // TX, RX
DFRobotDFPlayerMini myDFPlayer;

//
void setup () {
	mySoftwareSerial.begin(9600);
  Serial.begin(115200);

  Serial.println();
  Serial.println(F("DFRobot DFPlayer Mini Demo"));
  Serial.println(F("Initializing DFPlayer ... (May take 3~600 seconds)"));
  
  if (!myDFPlayer.begin(mySoftwareSerial)) {  //Use softwareSerial to communicate with mp3.
    Serial.println(F("Unable to begin:"));
    Serial.println(F("1.Please recheck the connection!"));
    Serial.println(F("2.Please insert the SD card!"));
    while(true){
      delay(0); // Code to compatible with ESP8266 watch dog.
    }
  }
  Serial.println(F("DFPlayer Mini online."));
  myDFPlayer.volume(30); //mettre le volume à 30 (max)
  myDFPlayer.play(1); //jouer la 1ère musique
}


void loop () {        
}