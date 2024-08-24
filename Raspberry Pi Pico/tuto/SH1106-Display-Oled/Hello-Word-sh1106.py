#ajouter le fichier "SH1106.py" à votre pico
from machine import I2C
from sh1106 import SH1106_I2C
import time

i2c = I2C(0) #changer la valeur permet de choisir sur quel broche on veut connecter l'écran
oled = SH1106_I2C(128,64, i2c) #definir la taille de l'écran et sa broche

oled.rotate(True)
oled.fill(0)
oled.text("hello", 5, 10)
oled.show()

while True:
    oled.fill(0)
    oled.text("hello", 5, 10)
    oled.show()
    time.sleep(1)
    oled.fill(0)
    oled.text("world !", 5, 10)
    oled.show()
    time.sleep(1)


