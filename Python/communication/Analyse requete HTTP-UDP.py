from flask import Flask, request, jsonify
import socket
import json
import threading

app = Flask(__name__)

# Définir les adresses et ports des serveurs
http_server_address = ('192.168.134.209', 8000)  # Adresse IP du serveur HTTP
udp_server_address = ('192.168.134.209', 9000)  # Adresse IP du serveur UDP
client_udp_address = ('localhost', 9001)  # Adresse IP et port du client UDP

# Créer un verrou pour éviter les problèmes de concurrence lors de l'accès aux données partagées
lock = threading.Lock()

# Liste pour stocker les données reçues
received_data = []


# Fonction pour gérer les requêtes UDP
def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.bind(udp_server_address)
        print(f"Serveur UDP en écoute sur {udp_server_address}")
        while True:
            data, addr = udp_socket.recvfrom(1024)
            payload = json.loads(data.decode('utf-8'))
            with lock:
                received_data.append(payload)
                print(f"Payload UDP reçu de {addr}: {payload}")


# Route HTTP pour recevoir des données
@app.route('/controls', methods=['POST'])
def handle_route1():
    try:
        # Récupérer le payload en qqqqtant que dictionnaire JSON
        payload = request.get_json()

        # Afficher le contenu du payload
        print(f"Payload reçu via HTTP : {payload}")

        # Envoyer la payload via UDP au client
        send_udp_request(payload, client_udp_address)

        # Vous pouvez effectuer des opérations supplémentaires avec le payload ici

        return jsonify({"message": "POST reçu avec succès!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Fonction pour envoyer la payload via UDP
def send_udp_request(payload, client_address):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        # Convertir le payload en chaîne JSON
        json_payload = json.dumps(payload)
        # Envoyer la payload au client UDP
        udp_socket.sendto(json_payload.encode('utf-8'), client_address)


def main():
    # Démarrez le serveur UDP dans un thread séparé
    udp_thread = threading.Thread(target=udp_server)
    udp_thread.start()

    # Démarrez le serveur HTTP
    app.run(host=http_server_address[0], port=http_server_address[1])

    #send_udp_request("aaaaa", client_udp_address)


if __name__ == '__main__':
    main()