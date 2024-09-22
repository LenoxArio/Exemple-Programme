/*
1) Brancher le module bluetooth sur l'arduino:

 bluetooth: RX <- TX :arduino
 bluetooth: TX -> RX :arduino

2) Créer votre application sur Mit App Inventor (exemple)
puis connecter vous au module.

*/

char Incoming_value = 0; //créer une chaine de caractère null

void setup() {
  Serial.begin(9600); //définir la vitesse serial à 9600 bauds
}

void loop() {
  if(Serial.available() > 0){ //si un message à été reçu via serial alors ...
    Incoming_value = Serial.read(); //lire ce que à reçu serial et mettre le message dans la variable: Incoming_value
    Serial.println(Incoming_value); //afficher le message dans le moniteur série
    if(Incoming_value == "hello"){  //si le message est hello alors ...
      Serial.println("hello"); //afficher hello dans le moniteur série
    }
  }
}
