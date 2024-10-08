import RPi.GPIO as GPIO
import time


#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
GPIO.setwarnings(False) #Disable warnings

#Use pin 12 for PWM signal
pwm_gpio = 12 #GPIO 18
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

#commencer a 0°
pwm.start(angle_to_percent(0))
time.sleep(1)

#tourner à 90°
pwm.ChangeDutyCycle(angle_to_percent(90))
time.sleep(1)

#tourner à 180°
pwm.ChangeDutyCycle(angle_to_percent(180))
time.sleep(1)

#Close GPIO & cleanup
pwm.stop()
GPIO.cleanup()