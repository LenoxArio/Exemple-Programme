import paho.mqtt.client as mqtt

# Configuration du client MQTT
broker_address = "192.168.1.41"  # Remplacez par l'adresse de votre serveur MQTT si nécessaire
topic = "hello/pico"

# Fonction de rappel pour la publication de messages
def publish_message():
    client.publish(topic, "Hello from PC!")

# Connexion au serveur MQTT
client = mqtt.Client()
client.connect(broker_address)

# Publier le message "Hello"
publish_message()

# Déconnecter du serveur MQTT
client.disconnect()
