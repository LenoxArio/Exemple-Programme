import time
from machine import Pin

button = Pin(18, Pin.IN, Pin.PULL_UP) #definir pin 18 INPUT et pour interrupteur

led = Pin(15, Pin.OUT)
led.value(0)

while True:
    if button.value() == 0:
        print("Button is Pressed")
        led.value(1)
        time.sleep(0.1)
    else:
        print("Button is not Pressed")
        led.value(0)
    time.sleep(0.1)

