import RPi.GPIO as GPIO
import time

# Définir les broches GPIO
TRIG_PIN = 23
ECHO_PIN = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

def distance_measurement():
    # Émettre une impulsion ultrasonique
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Enregistrez le temps actuel
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start_time = time.time()

    # Enregistrez le temps lorsque l'écho est reçu
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end_time = time.time()

    # Calculez la durée de l'impulsion ultrasonique
    pulse_duration = pulse_end_time - pulse_start_time

    # Utilisez la formule de distance pour convertir le temps en distance
    speed_of_sound = 34300  # en cm/s
    distance = (pulse_duration * speed_of_sound) / 2

    return distance

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        while True:
            dist = distance_measurement()
            print(f'Distance: {dist:.2f} cm')
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programme interrompu par l'utilisateur")
    finally:
        cleanup()
