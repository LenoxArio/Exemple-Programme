from picamera2 import Picamera2  # Importation de la bibliothèque Picamera2 pour utiliser la caméra Raspberry Pi
import cv2  # Importation de la bibliothèque OpenCV pour le traitement d'images
import numpy as np  # Importation de NumPy pour le traitement numérique des tableaux
from cv2 import aruco  # Importation du module ArUco de OpenCV pour la détection des marqueurs
import time  # Importation du module time pour gérer les temporisations

# Initialiser une instance de la caméra Picamera2
picam2 = Picamera2()

# Configurer la résolution de l'image capturée par la caméra
picam2.preview_configuration.main.size = (1920, 1080)

# Configurer le format de l'image capturée (ici, RGB888 signifie une image RGB 8 bits par canal)
picam2.preview_configuration.main.format = "RGB888"

# Démarrer la caméra pour la capture d'images
picam2.start()

# Obtenir un dictionnaire de marqueurs ArUco spécifiques (ici, 5x5 avec 1000 identifiants différents)
dictionary = aruco.Dictionary_get(aruco.DICT_5X5_1000)

# Créer les paramètres du détecteur de marqueurs ArUco
parameters = aruco.DetectorParameters_create()

# Boucle infinie pour capturer et traiter les images en continu
while True:
    # Capturer une image de la caméra sous forme de tableau NumPy
    im = picam2.capture_array()

    # Convertir l'image capturée en niveaux de gris, nécessaire pour la détection des marqueurs ArUco
    gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

    # Détecter les marqueurs ArUco dans l'image en niveaux de gris
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dictionary, parameters=parameters)

    # Vérifier si des marqueurs ArUco ont été détectés
    if ids is not None and len(ids) > 0:
        # Aplatir le tableau des identifiants des marqueurs détectés
        ids = ids.flatten()

        # Vérifier si l'identifiant '1' est présent parmi les marqueurs détectés
        if 1 in ids:
            print("Aruco détecté !")  # Afficher un message si le marqueur avec l'identifiant '1' est détecté
            time.sleep(1)  # Attendre une seconde avant de continuer

    # Afficher l'image capturée dans une fenêtre (décommenter la ligne suivante si nécessaire)
    # cv2.imshow("preview", im)

    # Vérifier si la touche 'q' est pressée pour quitter la boucle et arrêter la capture
    if cv2.waitKey(1) == ord('q'):
        break

# Arrêter la caméra Picamera2
picam2.stop()

# Fermer toutes les fenêtres créées par OpenCV
cv2.destroyAllWindows()
