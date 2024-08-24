
import serial
import time
from pynput.keyboard import Key, Controller
import pyautogui

# Remplacez 'COMx' par le port série de votre Arduino (par exemple, 'COM3' sur Windows ou '/dev/ttyACM0' sur Linux)
arduino_port = 'COM3'

keyboard = Controller()

def type_phrase(phrase):
    pyautogui.write(phrase, interval=0.0001)
def type_t():
    keyboard.press('t')
    time.sleep(0.1)  # Maintenir la touche enfoncée pendant 0.1 seconde
    keyboard.release('t')

def type_z():
    type_phrase("/spawn")

def type_e():
    keyboard.press(Key.enter)
    time.sleep(0.1)  # Maintenir la touche enfoncée pendant 0.1 seconde
    keyboard.release(Key.enter)


try:
    arduino = serial.Serial(arduino_port, 9600, timeout=1)
    print("Connexion établie avec l'Arduino sur le port", arduino_port)

    while True:
        data = arduino.readline().strip().decode('utf-8')
        if data == '0':
                type_t()
                type_z()
                type_e()

        
            
except KeyboardInterrupt:
    arduino.close()
    print("Connexion à l'Arduino interrompue.")
