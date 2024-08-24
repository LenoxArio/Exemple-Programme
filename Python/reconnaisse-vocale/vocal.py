import speech_recognition as sr
import pygame


pygame.mixer.init()
audio_file = 'voice.mp3'  # Remplacez par le chemin de votre fichier audio
pygame.mixer.music.load(audio_file)

def main():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Dites quelque chose...")
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("Vous avez dit : " + text)

                if "take a photo" in text.lower():
                    print("photo prise")
                if "how are you" in text.lower():
                    pygame.mixer.music.play(1)
            except sr.UnknownValueError:
                print("Impossible de comprendre l'audio")
            except sr.RequestError as e:
                print("Erreur de requête : {0}".format(e))

if __name__ == "__main__":
    main()
