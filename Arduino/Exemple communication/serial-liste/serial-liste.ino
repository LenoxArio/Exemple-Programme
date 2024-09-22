int led = 3;
String inputString = "";  // Variable pour stocker les données série
int ledValue = 0;         // Variable pour stocker la valeur de la LED

void setup() {
  Serial.begin(115200);   // Initialisation du port série
  pinMode(led, OUTPUT);   // Définir la broche LED en mode sortie
  analogWrite(led, 0);    // Éteindre la LED au démarrage
}

void loop() {
  // Vérifie si des données sont disponibles dans le buffer série
  if (Serial.available() > 0) {
    inputString = Serial.readString();   // Lire les données série reçues
    inputString.trim();                  // Supprimer les espaces ou caractères invisibles

    // Vérifier le format attendu ["led","valeur"]
    if (inputString.startsWith("[\"led\",\"") && inputString.endsWith("\"]")) {
      // Extraire la valeur entre les guillemets
      String valueString = inputString.substring(8, inputString.length() - 2);
      ledValue = valueString.toInt();  // Convertir la chaîne en entier
      // Appliquer la valeur à la LED si elle est dans les limites (0 à 255)
      if (ledValue >= 0 && ledValue <= 255) {
        analogWrite(led, ledValue);  // Mettre à jour la LED avec la valeur
      }
    } 
    // Vérifier le format attendu ["vitesse","valeur"]
    else if (inputString.startsWith("[\"vitesse\",\"") && inputString.endsWith("\"]")) {
      // Extraire la valeur entre les guillemets
      String valueString = inputString.substring(12, inputString.length() - 2);
      int v = valueString.toInt();  // Convertir la chaîne en entier

      Serial.print("La vitesse du moteur est : ");
      Serial.println(v);
    }
  }
}
