from speech_recognition import Recognizer, Microphone
import pygame
import time
pygame.mixer.init()
audio_file = 'ElevenLabs.mp3'
audio_file2 = 'SpeechOn.wav'  # Remplacez par le chemin de votre fichier audio
pygame.mixer.music.load(audio_file)
pygame.mixer.music.load(audio_file2)

recognizer = Recognizer()

# On enregistre le son

with Microphone() as source:
    print("Réglage du bruit ambiant... Patientez...")
    recognizer.adjust_for_ambient_noise(source)
    pygame.mixer.music.play(2)
    print("Vous pouvez parler...")
    recorded_audio = recognizer.listen(source)
    print("Enregistrement terminé !")
    
# Reconnaissance de l'audio

try:
    print("Reconnaissance du texte...")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="fr-FR"
        )
    if text == "salut" or text == "bonjour" or text == "salut ça va" or text == "bonjour ça va":
        print(text)
        pygame.mixer.music.play(1)
    print("Vous avez dit : {}".format(text))
    time.sleep(3)
except Exception as ex:
    print(ex)