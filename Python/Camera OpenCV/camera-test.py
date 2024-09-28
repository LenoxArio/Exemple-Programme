#ce code permet juste de voir si vous arriver à obtenir le flux vidéo de votre camera avec opencv et puis l'afficher
#Installer OpenCV : pip3 install opencv-python

import cv2

# Ouvre la caméra (indice 0 pour la webcam par défaut)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra")
    exit()

while True:
    # Capture image frame par frame
    ret, frame = cap.read()

    if not ret:
        print("Erreur : impossible de lire l'image de la caméra")
        break

    # Affiche l'image en direct
    cv2.imshow('Camera en Direct', frame)

    # Sort si l'utilisateur appuie sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère la caméra et ferme les fenêtres
cap.release()
cv2.destroyAllWindows()
