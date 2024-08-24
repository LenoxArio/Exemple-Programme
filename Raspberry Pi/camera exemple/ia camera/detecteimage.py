import cv2
import numpy as np
import time  # Ajout de l'importation pour le module time

# Adresse IP et port du serveur Raspberry Pi
server_ip = "192.168.1.38"  # Remplacez par l'adresse IP du Raspberry Pi
server_port = 12345          # Remplacez par le port spécifié sur le Raspberry Pi

# URL pour le flux vidéo UDP
udp_url = f"udp://{server_ip}:{server_port}"

print("Démarrage")
# Ouvrir la capture vidéo en utilisant l'URL UDP
try:
    cap = cv2.VideoCapture(udp_url)
except Exception as e:
    print(f"Erreur lors de l'ouverture de la capture vidéo : {e}")
    exit()

# Boucle pour lire et afficher les images du flux vidéo
while True:
    ret, frame = cap.read()

    if not ret:
        print("Erreur: Impossible de lire la trame.")
        break

    cv2.imshow("Flux vidéo Raspberry Pi", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(0.1)  # Ajouter un délai

# Libérer la capture vidéo et fermer la fenêtre
cap.release()
cv2.destroyAllWindows()
