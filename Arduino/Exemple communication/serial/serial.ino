int led = 2;

void setup() {
  Serial.begin(115200); // Initialise le port série pour la surveillance
  pinMode(led, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String receivedString = Serial.readStringUntil('\n'); // Lire la chaîne jusqu'à '\n'
    Serial.println(receivedString);
    // Comparer la chaîne reçue
    if (receivedString.equals("on")) {
      digitalWrite(led, HIGH); // Allumer le LED
      Serial.println("LED allumé");
    } else if (receivedString.equals("off")) {
      digitalWrite(led, LOW); // Éteindre le LED
      Serial.println("LED éteint");
    }
  }
}
