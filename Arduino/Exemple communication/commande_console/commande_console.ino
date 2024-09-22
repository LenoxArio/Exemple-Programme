
int led = 3;
int buzz = 2;

void setup() {
  Serial.begin(9600); // Initialise la communication série à 9600 bauds
  pinMode(led, OUTPUT);
  pinMode(buzz, OUTPUT); 
}

void loop() {
  if (Serial.available()) { // Vérifie si des données sont disponibles
    String input = Serial.readStringUntil('\n'); // demande un mot
    // Affiche la ligne de texte saisie sur le moniteur série
    Serial.print("Commande : ");
    Serial.println(input);

    // Découpe la ligne en mots et les affiche séparément
  

    if(input == "led on"){
      digitalWrite(led, HIGH);
    }
    if(input == "led off"){
      digitalWrite(led, LOW);
    }
    if(input == "buzz"){  //si le mot est buzz alors execute
       while (!Serial.available()) {
         Serial.print("Tone :"); 
         delay(100);
         int number = Serial.parseInt(); //demande un nombre
         tone(buzz, number, 500);
        }
        }

        
  }
}
