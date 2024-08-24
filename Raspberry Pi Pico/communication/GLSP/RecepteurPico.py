from machine import Pin
import time

INPUT = 19
OUTPUT = 18

button = Pin(INPUT, Pin.IN, Pin.PULL_UP)
led = Pin("LED", Pin.OUT)
signal = Pin(OUTPUT, Pin.OUT)


Bi = 0
def Binary(number):
    global Bi
    reçu = 0
    Bi = 0
    for i in range(number): 
        if button.value() == 0:
            print("1")
            signal.value(1)
            time.sleep(0.002)
            signal.value(0)
            Bi += 1  # Ajoutez un 1 à la position actuelle

        else:
            print("0")

        time.sleep(0.005)

test = 0
echec = 0

while True:
    if button.value() == 0:
        print("Lancement")
        Binary(8)#faire en sorte qu'il détecte 8 demande
        
    else:
        '''if Bi == 4:
            led.value(1)
            time.sleep(3)
            led.value(0)
        elif Bi == 5:
            led.value(1)
            time.sleep(0.5)
            led.value(0)
            time.sleep(0.5)'''
        if Bi == 6:
            test += 1
        elif (Bi <= 5 or Bi >= 7) and Bi >=2 and Bi <= 8:
            print(Bi)
            led.value(0)
            echec += 1
            print("resulta =",test, "echec=",echec)
        
        time.sleep(0.05)



