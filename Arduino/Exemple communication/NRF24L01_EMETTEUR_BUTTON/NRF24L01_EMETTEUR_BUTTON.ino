/*
Emeteur: si on clique sur le bouton
on envoie 'RERT' qui allume la led sur
l'autre arduino mais si il est pas presser on envoie
'stop' | Bouton = broche 2 / D2

*/
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
int but = 2;
int val;

//create an RF24 object
RF24 radio(9, 8);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";

void setup()
{
  radio.begin();
  pinMode(but, INPUT);
  //set the address
  radio.openWritingPipe(address);
  
  //Set module as transmitter
  radio.stopListening();
}
void loop()
{
  val = digitalRead(but);
  if(val == LOW){
  const char text[] = "RERT";
  radio.write(&text, sizeof(text));
  delay(2000);
  }
  const char text[] = "stop";
  radio.write(&text, sizeof(text));
  
  delay(100);
}