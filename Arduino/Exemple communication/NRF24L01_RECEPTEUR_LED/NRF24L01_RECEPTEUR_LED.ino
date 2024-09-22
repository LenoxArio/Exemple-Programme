//Include Libraries
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
int led = 2;

//create an RF24 object
RF24 radio(9, 8);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";

void setup()
{
  while (!Serial);
    Serial.begin(9600);
  
  radio.begin();
 pinMode(led, OUTPUT); 
  //set the address
  radio.openReadingPipe(0, address);
  
  //Set module as receiver
  radio.startListening();
}

void loop()
{
  //Read the data if available in buffer
  if (radio.available())
  {
     char text[32] = {0};  // Déclarez la variable 'text' ici
    radio.read(&text, sizeof(text));
    Serial.println(text);

    if (strcmp(text, "RERT") == 0)  // Utilisez strcmp pour comparer les chaînes de caractères
    {
      digitalWrite(led, HIGH);
    }
    else if(strcmp(text, "stop") == 0)
    {
      digitalWrite(led, LOW);
    }
  }
}