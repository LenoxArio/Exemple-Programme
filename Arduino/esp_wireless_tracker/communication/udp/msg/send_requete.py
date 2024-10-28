import socket
import time

addrPort = ("192.168.1.103", 1234)
bufferSize = 1024

# Créer un socket UDP coté client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    s.sendto(str.encode("ledOn"), addrPort)
    time.sleep(0.3)
    s.sendto(str.encode("ledOff"), addrPort)
    time.sleep(1)
