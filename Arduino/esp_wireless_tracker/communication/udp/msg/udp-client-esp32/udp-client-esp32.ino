#include <WiFi.h>
#include <WiFiUdp.h>

// Configuration Wi-Fi
const char* ssid = "Freebox-1E0914";        // Remplace par ton SSID
const char* password = "k69d6qv43wqnf55nqhkdxm"; // Remplace par ton mot de passe

#define LED 18

// Configuration UDP
WiFiUDP udp;
const unsigned int localUdpPort = 1234;  // Le port sur lequel écouter
char incomingPacket[255];                // Tampon pour les messages reçus

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  // Connexion au Wi-Fi
  Serial.printf("Connexion au Wi-Fi: %s\n", ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Tentative de connexion...");
  }
  
  Serial.println("Connecté au Wi-Fi!");
  Serial.print("Adresse IP: ");
  Serial.println(WiFi.localIP());

  // Démarrage du serveur UDP
  udp.begin(localUdpPort);
  Serial.printf("Serveur UDP démarré. Écoute sur le port %d\n", localUdpPort);
}

void loop() {
  // Vérifie si un paquet UDP a été reçu
  int packetSize = udp.parsePacket();
  if (packetSize) {
    Serial.printf("Paquet reçu, taille: %d\n", packetSize);
    
    // Lit le paquet UDP
    int len = udp.read(incomingPacket, 255);
    if (len > 0) {
      incomingPacket[len] = '\0';  // Termine la chaîne
    }
    Serial.printf("Contenu: %s\n", incomingPacket);
    if(strcmp(incomingPacket, "ledOn") == 0){
      digitalWrite(LED, HIGH);
    }else if(strcmp(incomingPacket, "ledOff") == 0){
      digitalWrite(LED, LOW);
    }
    // Répond au client (facultatif)
    udp.endPacket();
  }
}
