import serial
import time

# Définir le port série
ser = serial.Serial('/dev/ttyS0', 9600) 
print("GPIO OK")

while True:
    # Lire depuis le port série
    if ser.in_waiting > 0:
        data = ser.readline()
        print(data.decode().strip())

    # Écrire vers le port série
    ser.write(b'Hello Pico\n')

    time.sleep(1)
