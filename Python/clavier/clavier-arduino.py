import serial
import time
from pynput.keyboard import Key, Controller

# Remplacez 'COMx' par le port série de votre Arduino (par exemple, 'COM3' sur Windows ou '/dev/ttyACM0' sur Linux)
arduino_port = 'COM3'

keyboard = Controller()

def type_z():
    keyboard.press('z')
    time.sleep(0.1)  # Maintenir la touche enfoncée pendant 0.1 seconde
    keyboard.release('z')


try:
    arduino = serial.Serial(arduino_port, 9600, timeout=1)
    print("Connexion établie avec l'Arduino sur le port", arduino_port)

    while True:
        data = arduino.readline().strip().decode('utf-8')
        if data == '0':
                type_z()

        
            
except KeyboardInterrupt:
    arduino.close()
    print("Connexion à l'Arduino interrompue.")
