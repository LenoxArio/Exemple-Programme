import keyboard

def on_up_arrow_press(event):
    print("hello")

# Assigner la fonction à la touche flèche du haut
keyboard.on_press_key("up", on_up_arrow_press)

print("Appuyez sur la touche flèche du haut pour afficher 'hello'. Appuyez sur 'esc' pour quitter.")

# Boucle infinie pour garder le programme en cours d'exécution
try:
    while True:
        # Écoute la touche 'esc' pour quitter le programme
        if keyboard.is_pressed('esc'):
            print("Programme terminé.")
            break
except KeyboardInterrupt:
    print("Programme interrompu.")
