import RPi.GPIO as GPIO
import time

def angles (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


GPIO.setmode(GPIO.BCM) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings


pwm_gpio = 18 
frequence = 50
but = 2
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)
GPIO.setup(but, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pwm.start(angles(90))
time.sleep(1)
#commencer a 0°
while True:
    val = GPIO.input(but)

    if(val == 0):
        pwm.ChangeDutyCycle(angles(0))
        time.sleep(1)
    else:
        pwm.ChangeDutyCycle(angles(180))
