#include <WiFi.h>

const char* ssid = "Freebox-1E0914";
const char* password = "k69d6qv43wqnf55nqhkdxm";

void setup()
{
	Serial.begin(115200);
	delay(1000);
  Serial.print("ESP Connected !");
	Serial.println("\n");
	
	WiFi.begin(ssid, password);
	Serial.print("Tentative de connexion...");
	
	while(WiFi.status() != WL_CONNECTED)
	{
		Serial.print(".");
		delay(100);
	}
	
	Serial.println("\n");
	Serial.println("Connexion etablie!");
	Serial.print("Adresse IP: ");
	Serial.println(WiFi.localIP());
}

void loop()
{
	
}