#Ce code pour permet de détecter les marqueurs aruco en 5x5 et de faire un carré vert autour
#il affiche la valeur dans la console
#Installer OpenCV : pip3 install opencv-python
#Vous pouvez changer le type d'aruco à cette ligne : dictionary = aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
#Pour tester ce code utiliser ce site : https://chev.me/arucogen/

import cv2
from cv2 import aruco

# Ouvre la caméra (indice 0 pour la webcam par défaut)
cap = cv2.VideoCapture(0)

# Charge le dictionnaire ArUco et les paramètres du détecteur
dictionary = aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(dictionary, parameters)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra")
    exit()

while True:
    # Capture image frame par frame
    ret, frame = cap.read()
    if not ret:
        print("Erreur : impossible de lire l'image de la caméra")
        break

    # Convertir l'image en niveaux de gris pour la détection ArUco
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Détection des marqueurs ArUco
    corners, ids, rejectedImgPoints = detector.detectMarkers(gray)

    # Si des marqueurs sont détectés
    if len(corners) > 0:
        ids = ids.flatten()
        print(ids)
        for corner, marker_id in zip(corners, ids):
            # Dessine un carré vert autour du marqueur
            corner = corner.reshape((4, 2))
            (top_left, top_right, bottom_right, bottom_left) = corner

            # Convertir les coordonnées en entiers
            top_left = tuple(map(int, top_left))
            top_right = tuple(map(int, top_right))
            bottom_right = tuple(map(int, bottom_right))
            bottom_left = tuple(map(int, bottom_left))

            # Dessine les lignes du carré
            cv2.line(frame, top_left, top_right, (0, 255, 0), 2)
            cv2.line(frame, top_right, bottom_right, (0, 255, 0), 2)
            cv2.line(frame, bottom_right, bottom_left, (0, 255, 0), 2)
            cv2.line(frame, bottom_left, top_left, (0, 255, 0), 2)

            # Position pour afficher l'identifiant du marqueur
            cX = int((top_left[0] + bottom_right[0]) / 2)
            cY = int((top_left[1] + bottom_right[1]) / 2)

            # Affiche l'identifiant du marqueur sur l'image
            cv2.putText(frame, str(marker_id), (cX - 10, cY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if ids == 5: #si la valeur du marqueur (aruco) = 5 alors 
                print("Number 5 detecter Danger")
    # Affiche l'image en direct
    cv2.imshow('Camera en Direct', frame)

    # Sort si l'utilisateur appuie sur 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère la caméra et ferme les fenêtres
cap.release()
cv2.destroyAllWindows()
