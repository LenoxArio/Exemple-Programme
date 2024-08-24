import network
import socket
from time import sleep
from machine import Pin

ssid = 'SSID'
password = 'PASSWORD'
    
    
def connect(): #se connecter au réseau grâce aux info de ssid et password
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def server():
    global ip
    
    UDP_IP = ip
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)
        
        if data == b'ok':
            print("hello")

ip = connect()
server()
    



