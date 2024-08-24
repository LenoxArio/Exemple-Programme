import RPi.GPIO as GPIO
import time

pinBtn = 2
led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(pinBtn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


while True:
    etat = GPIO.input(pinBtn)

    if(etat == 0):
        GPIO.output(led,GPIO.HIGH)
        time.sleep(0.1)
    else:
        GPIO.output(led,GPIO.LOW)
        time.sleep(0.1)
