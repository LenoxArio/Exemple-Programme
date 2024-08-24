import time
import socket
import json

# Adresse et port du serveur UDP
udp_server_address = ('192.168.1.103', 5000)  # Adresse IP du serveur UDP

# Liste pour stocker les données à envoyer
data_to_send = [
    ["moteur", "1"],
    ["direction", "1"],
    ["speed", "18"]
]

# Fonction pour envoyer la payload via UDP
def send_udp_request(payload, client_address):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        # Convertir le payload en chaîne JSON
        json_payload = json.dumps(payload)
        # Envoyer la payload au client UDP
        udp_socket.sendto(json_payload.encode('utf-8'), client_address)

# Fonction principale pour envoyer les données périodiquement
def main():
    while True:
        send_udp_request(data_to_send, udp_server_address)
        time.sleep(1)

if __name__ == '__main__':
    main()
