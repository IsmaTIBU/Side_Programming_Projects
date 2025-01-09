import cv2
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


# Cargar el modelo entrenado
autoencoder = load_model("autoencoder_esfera_roja.h5")

# Función para preprocesar imágenes
def preprocesar_imagen(frame):
    imagen = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir BGR a RGB
    imagen = cv2.resize(imagen, (128, 128))  # Redimensionar
    imagen = np.array(imagen) / 255.0  # Normalizar
    return imagen

# Función para detectar esferas rojas en un frame
def detectar_esfera(frame):
    preprocesada = preprocesar_imagen(frame)
    reconstruida = autoencoder.predict(preprocesada.reshape(1, 128, 128, 3))
    error = np.mean((preprocesada - reconstruida[0])**2)

    # Umbral para detección de esferas rojas (ajustar según necesidad)
    return error < 0.005

# Dibujar bounding box alrededor de la esfera roja
def dibujar_bounding_box(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Crear máscara para el color rojo
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2

    # Encontrar contornos de la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Filtrar pequeñas áreas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Procesar video y detectar esferas rojas
def procesar_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if detectar_esfera(frame):
            dibujar_bounding_box(frame)

        out.write(frame)
        cv2.imshow('Detección de Esferas Rojas', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Ejecutar el programa
video_path = "C:/Users/01ism/OneDrive/Desktop/video coche.mp4"  # Cambia esta ruta al video que deseas procesar
output_path = "C:/Users/01ism/OneDrive/Desktop/Programas/Python/FS__PercepSimu/FS_Simu/output_video.avi"  # Ruta del video de salida
procesar_video(video_path, output_path)
