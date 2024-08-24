import keyboard
import pyautogui
import socket
import time


raspberry_pi_ip = '192.168.1.24'  # Remplacez par l'adresse IP réelle du Raspberry Pi
raspberry_pi_port = 25565  # Utilisez le port que vous avez spécifié sur le Raspberry Pi

# Créez un socket client pour se connecter au Raspberry Pi
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((raspberry_pi_ip, raspberry_pi_port))

def envoyer_commande(commande):
    client_socket.send(commande.encode())

# Définir une position initiale de la souris
last_x = pyautogui.position().x
tolerance = 5  # Marge de tolérance pour éviter les changements trop sensibles

start_y = pyautogui.position().y
angle = 90

time.sleep(15)

while True:
    current_x = pyautogui.position().x
    current_y = pyautogui.position().y

    if current_x < last_x - tolerance:
        print("gauche")
        envoyer_commande('g')
        time.sleep(0.1)
    if current_x > last_x + tolerance:
        print("droite")
        envoyer_commande('d')
        time.sleep(0.1)

    if current_y < start_y:
        # Déplacement vers le haut
        angle += 1
    if current_y > start_y:
        # Déplacement vers le bas
        angle -= 1

    #touche =============================================
    if keyboard.is_pressed('z'):
        print("avancer")
        envoyer_commande('a')
        time.sleep(0.1)
    
    if keyboard.is_pressed('s'):
        print("recule")
        envoyer_commande('r')
        time.sleep(0.1)

    if keyboard.is_pressed('d'):
        print("droite")
        envoyer_commande('d')
        time.sleep(0.1)

    if keyboard.is_pressed('q'):
        print("gauche")
        envoyer_commande('g')
        time.sleep(0.1)
    #touche =============================================
    envoyer_commande('s')
    time.sleep(0.01)

    
    last_x = current_x
    start_y = current_y

    # Sortir de la boucle si la touche "q" est enfoncée
    if keyboard.is_pressed("e"):
        break
