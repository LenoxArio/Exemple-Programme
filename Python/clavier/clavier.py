import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def type_z():
    keyboard.press('z')
    time.sleep(0.1)  # Maintenir la touche enfoncée pendant 0.1 seconde
    keyboard.release('z')

if __name__ == "__main__":
    interval = 3  # 3 secondes
    while True:
        type_z()
        time.sleep(interval)
