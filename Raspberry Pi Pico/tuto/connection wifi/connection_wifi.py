from machine import Pin
import time
import network
import socket

ssid = 'SSID' #nom du réseau
password = 'PASSWORD' #Mot de Passe du réseau

def connect():  #fonction qui permet de se connecter au réseau
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password) #se connecter à la box grâce au variable ssid et password
    while wlan.isconnected() == False: #si il n'est toujours pas connecter alors
        print('Waiting for connection...')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}') #afficher "Connected on" + afficher l'ip du pico
    return ip



ip = connect()
