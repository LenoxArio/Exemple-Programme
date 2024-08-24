'''
code fait par Raspberry pi et modifier par lenox.
Ce code permet de créer une page web avec 2 bouton: on et off il communique avec le code  python pour envoyer une requête lorsque un des 2 bouton est pressé
cela permet donc de soit allume/éteindre une led 

'''

import network
import socket
from time import sleep
from machine import Pin

led = Pin(15, Pin.OUT)
ssid = 'SSID'  #Nom du wifi
password = 'PASSWORD' #Mot de pass du wifi

led.value(0)

def connect():  # se connecter au réseau grâce aux info de ssid et password
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip


def webpage():  # créer le site internet en HTML
    # Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
                <form action="./lighton?">
                <input type="submit" value="Allumer la led" />
                </form>

                <form action="./lightoff?">
                <input type="submit" value="Eteindre la led" />
                </form>

            </body>
            </html>
            """
    return str(html)


def open_socket(ip):  # ouvrir les port en 80
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def serve(connection):  # mettre le site en ligne et tester


    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':  # si l'url est "192.168.1.41/lighton?" alors
            led.value(1)

        elif request == '/lightoff?':  # sinon si l'url est "192.168.1.41/lightoff?" alors
            led.value(0)

        html = webpage()
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    print("stop")


