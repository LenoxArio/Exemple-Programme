import network
import socket
import ujson
import time
from machine import Pin

ssid = 'Freebox-1E0914'
password = 'k69d6qv43wqnf55nqhkdxm'

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 5000))
    print("starting")
    
    while True:
        data, addr = udp_socket.recvfrom(1024)
        command = ujson.loads(data.decode())
        #print(command)
        
        # Assumer que command est une liste de listes
        data_dict = {item[0]: item[1] for item in command}
        
       
        direction1 = data_dict.get("direction1")
        speed1 = data_dict.get("speed1")
        
        direction2 = data_dict.get("direction2")
        speed2 = data_dict.get("speed2")
        
        if direction1 == '1':
            print("vitesse :", speed1)
            
        if direction2 == '1':
            print("vitesse :", speed2)
        
ip = connect()
server()

