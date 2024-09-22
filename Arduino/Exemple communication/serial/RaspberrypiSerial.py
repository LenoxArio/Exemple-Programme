'''
A LIRE:
    configurer pour l'uart:
    1) Tapper: sudo nano /boot/firmware/cmdline.txt
    "Retier le firmware si ça marche pas"
    2) Retirer cette ligne: console=serial0,115200
    3) Redémarrer le raspberry pi

    4) Tapper: sudo raspi-config
    5) Aller dans: Interface Options
    6) Aller dans: "Serial Port"  et mettez Yes ou Oui
    7) Reboot

'''


import serial
import time

# Configuration du port série
serial_port = '/dev/ttyS0'  # Changez ceci en fonction de votre configuration
baud_rate = 115200  # Vitesse de communication (bauds)

try:
    # Initialisation de la connexion série
    ser = serial.Serial(serial_port, baud_rate)
    print(f"Connexion série ouverte sur {serial_port} à {baud_rate} bauds")
    
    # Attente de l'ouverture du port série
    time.sleep(2)

    def send(message):
        ser.write((message + '\n').encode())  # Ajouter un caractère de fin de ligne
        print(f"Message envoyé : {message}")

    # Envoyer des commandes "on" et "off" en alternance
    while True:
        send("on")
        time.sleep(1)
        send("off")
        time.sleep(1)

except serial.SerialException as e:
    print(f"Erreur de connexion au port série : {e}")

finally:
    if ser.is_open:
        ser.close()
        print("Connexion série fermée")
