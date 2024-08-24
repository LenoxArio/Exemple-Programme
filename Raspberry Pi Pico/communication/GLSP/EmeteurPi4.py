import RPi.GPIO as GPIO
import time


OUTPUT = 18
INPUT = 21



GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT, GPIO.OUT)
GPIO.setup(INPUT, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.output(OUTPUT,True)


def encoder(number):
    GPIO.output(OUTPUT,False)
    time.sleep(0.02)
    GPIO.output(OUTPUT,True)
    for i in range(number):
        etat = GPIO.input(INPUT)
        GPIO.output(OUTPUT,False)
        while (etat == 0):
            etat = GPIO.input(INPUT)
        
        GPIO.output(OUTPUT,True)
        time.sleep(0.005)

while True:
    nombre = int(input("Entrez un nombre : "))
    encoder(nombre)