import socket
import time

# Configuration de la socket UDP
addrPort = ("0.0.0.0", 1234)
bufferSize = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addrPort)  # Assure que la socket écoute sur le port spécifié

s.settimeout(0.1)  # Timeout de 100ms pour les tentatives de réception

def receive():
    global s
    try:
        data, addr = s.recvfrom(bufferSize)
        return data.decode("utf-8")
    except socket.timeout:
        return None

while True:
    received_data = receive()  # Réception non bloquante
    if received_data is not None:
        if received_data == "004":
            print("hello")

    time.sleep(0.1)
