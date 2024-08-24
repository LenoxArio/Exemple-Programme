import socket

msgClient = "h"
msgToSend = str.encode(msgClient)
addrPort = ("192.168.1.46", 9999)
bufferSize = 1024

# Créer un socket UDP coté client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Envoyer au serveur à l'aide du socket UDP créé
s.sendto(msgToSend, addrPort)
msgServer = s.recvfrom(bufferSize)

msg = "Message du serveur {}".format(msgServer[0])
print(msg)