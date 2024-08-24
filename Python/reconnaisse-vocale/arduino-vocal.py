import speech_recognition as sr
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)

def send_data(message):
    # Envoie le message au port série
    ser.write(message.encode('utf-8'))

def main():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Dites quelque chose...")
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("Vous avez dit : " + text)

                if "turn on the light" in text.lower():
                    print("photo prise")
                    send_data('o')
                if "turn off the light" in text.lower():
                    send_data('f')
                    
            except sr.UnknownValueError:
                print("Impossible de comprendre l'audio")
            except sr.RequestError as e:
                print("Erreur de requête : {0}".format(e))

if __name__ == "__main__":
    main()
