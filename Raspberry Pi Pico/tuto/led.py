import time
from machine import Pin #librairie pour les port gpio


led = Pin(15, Pin.OUT) #definir le pin 5 en OUTPUT et qui s'appelle led


while True:
	led.value(1) #allumer la led
    time.sleep(1) #attendre 1s
	led.value(0) #éteindre la led
    time.sleep(1) #attendre 1s