/*
Fait par Lenox95:

############LIB/Installation############
  Ce code permet d'utiliser un ecran oled SH1106 bicolore avec adafruit.
  Lien de la lib: https://github.com/wonho-maker/Adafruit_SH1106/tree/master
  Installer aussi la lib "Adafruit GFX Library" qui est dispo dans le gestionnaire des bibliothèques 

############Connection############
  Utiliser la broche A4 et A5 ou SDA et SCL/SCK

############Autre############
  utiliser "display.display();" pour afficher vos élement sur l'écran
*/


#include <Wire.h> //importer la lib "Wire"
#include <Adafruit_GFX.h> //importer la lib "Adafruit_GFX"
#include <Adafruit_SH1106.h> //importer la lib "Adafruit_SH1106"

#define OLED_RESET 4
Adafruit_SH1106 display(OLED_RESET);

void setup() {
  Serial.begin(9600); //définir serial sur 9600 bauds

  display.begin(SH1106_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3D (for the 128x64)
  display.clearDisplay(); //effacer l'écran

  display.setTextSize(1); //définir la police à 1
  display.setTextColor(WHITE); //mettre le texte en blanc
  display.setCursor(0, 0); //mettre le curseur à x=0, y=0
  display.println("Hello, world!"); //afficher "Hello, wordl!" sur l'écran
  display.display(); //afficher le texte sur l'écran
}

void loop() {
  display.setTextSize(1); //taille du texte
  display.setTextColor(WHITE); //couleur blanche
  display.setCursor(0, 0); //mettre position : 0 0
  display.println("Hello, world!"); //écrire Hello, world!
  display.display(); //apporter les modif
  delay(1000);
  display.clearDisplay(); // effacer l'écran
  delay(10);

  display.drawRect(10, 10, 50, 20, WHITE); // Dessiner un rectangle de 50x20 pixels à la position (10, 10)
  display.display();
  delay(1000);
  display.clearDisplay(); // effacer l'écran
  delay(10);

  display.fillRect(10, 10, 50, 20, WHITE); // Remplir un rectangle de 50x20 pixels à la position (10, 10)
  display.display();
  delay(1000);
  display.clearDisplay(); // effacer l'écran
  delay(10);

  display.drawCircle(30, 30, 10, WHITE); // Dessiner un cercle de rayon 10 à la position (30, 30)
  display.display();
  delay(1000);
  display.clearDisplay(); // effacer l'écran
  delay(10);

  display.drawTriangle(10, 10, 50, 10, 30, 40, WHITE); // Dessiner un triangle à partir des points (10, 10), (50, 10), et (30, 40)
  display.display();
  delay(1000);
  display.clearDisplay(); // effacer l'écran
  delay(10);

  display.drawPixel(10, 10, WHITE); //dessiner un pixel en 10-10
  display.display();
  delay(-1);

  // On peut changer draw "drawTriangle" par fill "fillTriangle" pour le remplire !
  
}