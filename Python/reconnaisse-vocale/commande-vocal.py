from speech_recognition import Recognizer, Microphone

import time


recognizer = Recognizer()


with Microphone() as source:
    print("Réglage du bruit ambiant... Patientez...")
    recognizer.adjust_for_ambient_noise(source)
    print("Vous pouvez parler...")
    recorded_audio = recognizer.listen(source)
    

try:
    print("Reconnaissance du texte...")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="fr-FR"
        )
    if text == "lenox allume la lumière":
        print("lumière alumé")
        time.sleep(3)
    if text == "lenox éteint la lumière":
        print("lumière éteint")
        time.sleep(3)
except Exception as ex:
    print(ex)