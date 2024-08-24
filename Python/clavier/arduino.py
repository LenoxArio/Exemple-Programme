import serial


# Remplacez 'COMx' par le port série de votre Arduino (par exemple, 'COM3' sur Windows ou '/dev/ttyACM0' sur Linux)
arduino_port = 'COM3'

try:
    arduino = serial.Serial(arduino_port, 9600, timeout=1)
    print("Connexion établie avec l'Arduino sur le port", arduino_port)

    while True:
        data = arduino.readline().strip().decode('utf-8')
        if data == '0':
            print("Le bouton est pressé!")

except KeyboardInterrupt:
    arduino.close()
    print("Connexion à l'Arduino interrompue.")
