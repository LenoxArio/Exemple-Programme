from machine import UART, Pin
import time

# Initialisation de l'UART sur le Raspberry Pi Pico
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Fonction pour envoyer des commandes au module MP3-TF-16P
def send_command(command):
    uart.write(command)
    time.sleep(0.1)  # Délai pour laisser le temps au module de traiter la commande

# Fonction pour choisir et jouer une musique spécifique
def play_track(track_number):
    # Convertir le numéro de piste en deux octets hexadécimaux
    track_number_high = track_number // 256
    track_number_low = track_number % 256
    # Commande pour jouer une piste spécifique
    command = bytes([0x7E, 0xFF, 0x06, 0x03, 0x00, track_number_high, track_number_low, 0xEF])
    send_command(command)

# Fonction pour arrêter la musique
def stop_music():
    # Commande pour arrêter la lecture
    stop_command = bytes([0x7E, 0xFF, 0x06, 0x16, 0x00, 0x00, 0x00, 0xEF])
    send_command(stop_command)

# Exemple d'utilisation
play_track(1)  # Remplacez 1 par le numéro de la piste que vous voulez jouer
time.sleep(5)  # Joue la musique pendant 10 secondes
stop_music()

