#ajouter le fichier "servo.py à votre pico. Vous pouvez aussi prendre le code de se fichier pour le mettre ce code"
from servo import Servo
import time

servo = Servo(pin=15)

while True:
    servo.move(0)
    time.sleep(1)
    servo.move(180)
    time.sleep(1)