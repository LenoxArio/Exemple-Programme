from machine import Pin, time_pulse_us
import time

SOUND_SPEED=340 # Vitesse du son dans l'air
TRIG_PULSE_DURATION_US=10

trig_pin = Pin(20, Pin.OUT) # Broche GP15 de la Pico
echo_pin = Pin(21, Pin.IN)  # Broche GP14 de la Pico

led = Pin(15, Pin.OUT)

while True:
    trig_pin.value(0)
    time.sleep_us(5)
    trig_pin.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig_pin.value(0)

    ultrason_duration = time_pulse_us(echo_pin, 1, 30000)  # Renvoie le temps de propagation de l'onde (en µs)
    distance_cm = SOUND_SPEED * ultrason_duration / 20000
    print(f"Distance : {distance_cm} cm")
    if distance_cm <= 7:
        led.value(1)
        time.sleep(0.1)
    else:
        led.value(0)
    time.sleep_ms(500)

