#il faut que vous télécharger le code source de Opencv  : https://github.com/opencv/opencv/releases  ensuite faite extraire et mettez le dans le même dossier que  se code.
#attention changer le "opencv-4.x" à ligne 16 par le nom du dossier de opencv par exemple : "opencv-4.10.0"


from picamera2 import Picamera2
import cv2
import numpy as np

# Initialiser la caméra
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1920, 1080)
picam2.preview_configuration.main.format = "RGB888"
picam2.start()

# Charger le classificateur Haar pour la détection des visages
face_cascade = cv2.CascadeClassifier('opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml') #!!!!! changer changer le "opencv-4.x" à ligne 16 par le nom du dossier de opencv par exemple : "opencv-4.10.0"

# Charger l'image de référence et extraire les descripteurs
reference_image = cv2.imread("obama_small.jpg")
reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
reference_faces = face_cascade.detectMultiScale(reference_gray, scaleFactor=1.1, minNeighbors=5)

# Assurez-vous qu'un seul visage est détecté dans l'image de référence
if len(reference_faces) != 1:
    raise ValueError("L'image de référence doit contenir exactement un visage.")

x, y, w, h = reference_faces[0]
reference_face = reference_gray[y:y+h, x:x+w]

# Initialiser le modèle de reconnaissance des visages d'OpenCV
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train([reference_face], np.array([0]))

def detect_and_recognize_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face)

        if label == 0 and confidence < 100:  # Vous pouvez ajuster le seuil de confiance
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Obama", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    
    return img

while True:
    im = picam2.capture_array()
    im = detect_and_recognize_face(im)

    cv2.imshow('Video', im)

    if cv2.waitKey(1) == ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()
