import RPi.GPIO as GPIO
import time

ledR = 14
ledJ = 15
ledG = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledR,GPIO.OUT)
GPIO.setup(ledJ,GPIO.OUT)
GPIO.setup(ledG,GPIO.OUT)

GPIO.output(ledJ,GPIO.LOW)
GPIO.output(ledR,GPIO.LOW)
GPIO.output(ledG,GPIO.LOW)
while True:
	GPIO.output(ledJ,GPIO.LOW)
	GPIO.output(ledR,GPIO.HIGH)
	time.sleep(5)
	GPIO.output(ledR,GPIO.LOW)
	GPIO.output(ledG,GPIO.HIGH)
	time.sleep(4)
	GPIO.output(ledG,GPIO.LOW)
	GPIO.output(ledJ,GPIO.HIGH)
	time.sleep(1)
