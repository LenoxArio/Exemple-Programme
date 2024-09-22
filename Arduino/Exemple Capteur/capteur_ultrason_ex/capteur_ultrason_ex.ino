


void setup()
{
  Serial.begin(9600);
}

void loop(){
  ultrason = 0.01723 * readUltrasonicDistance(2, 3);  //broche du capteur [2 = trig] & [3 = echo], appeler la fonction "readUltrasonicDistance" puis obtenir sa valeur puis la multiplier par 0.01723 et mettre ce résulta dans la variable : ultrason
  Serial.println(ultrason); //afficher la valeur de la varaible "ultrason" dans le moniteur série

  if (50 >= ultrason){ //si la valeur de "ultrason" est inférieur à 50 (50cm) alors ...
    Serial.println("Danger !!!"); //afficher "Danger !!!" dans le moniteur série
  } 
  delay(10);
}

long readUltrasonicDistance(int triggerPin, int echoPin){ //créer une fonction de type long avec la création de 2 variable d'entier : triggerPin,echoPin 
  pinMode(triggerPin, OUTPUT); //définir la broche de l'emetteur à ultrason à la valeur de "triggerPin" : Sortie
  digitalWrite(triggerPin, LOW); //envoyer un courant bas (off) à l'emetteur à ultrason 
  delayMicroseconds(2); //attendre 2 microsecondes
  digitalWrite(triggerPin, HIGH); //envoyer un courant haut (on) à l'emetteur à ultrason pour envoyer un ultrason
  delayMicroseconds(10); //attendre 10 microsecondes
  digitalWrite(triggerPin, LOW); //envoyer un courant bas (off) à l'emetteur à ultrason 
  pinMode(echoPin, INPUT); //définir la broche du récepteur à ultrason à la valeur de "echoPin" : Entrée
  return pulseIn(echoPin, HIGH); //renvoyer les pulsations obtenue du récepteur
}