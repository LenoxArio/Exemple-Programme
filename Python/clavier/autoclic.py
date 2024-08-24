import pyautogui
import time

time.sleep(2)

while True:
    pyautogui.mouseDown()

    # Attendre 0,1 seconde
    time.sleep(0.1)

    # Relâcher le clic gauche
    pyautogui.mouseUp()
    time.sleep(1)
