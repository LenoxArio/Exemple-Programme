#define LED_USER 18  // Broche de la led blanche "light user"

void setup() {
  pinMode(LED_USER, OUTPUT);  // Définir la broche LED comme sortie
}

void loop() {
  digitalWrite(LED_USER, HIGH);  // Allumer la LED
  delay(1000);              // Attendre 1 seconde
  digitalWrite(LED_USER, LOW);   // Éteindre la LED
  delay(1000);              // Attendre 1 seconde
}
