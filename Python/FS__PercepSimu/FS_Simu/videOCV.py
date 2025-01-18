import cv2
import numpy as np

# Función para procesar cada frame y detectar la bola roja
def detectar_bola_roja(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definir los rangos para el color rojo en HSV
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Crear máscaras para el color rojo
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2

    # Filtrar el ruido con operaciones morfológicas
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    # Encontrar contornos de los objetos detectados
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Filtrar áreas pequeñas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Bola roja", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return frame

# Procesar un video
def procesar_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)

    # Obtener dimensiones y FPS del video original
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Configurar el video de salida
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detectar la bola roja en el frame
        frame = detectar_bola_roja(frame)

        # Guardar el frame procesado en el video de salida
        out.write(frame)

        # Mostrar el frame procesado
        cv2.imshow('Detección de bola roja', frame)

        # Salir si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Ruta del video de entrada y salida
video_path = "C:/Users/01ism/OneDrive/Desktop/video coche.mp4"  # Cambia esto por la ruta de tu video
output_path = "C:/Users/01ism/OneDrive/Desktop/Programas/Python/FS__PercepSimu/FS_Simu/video_result.avi"  # Cambia esto por la ruta de salida

# Ejecutar el procesamiento del video
procesar_video(video_path, output_path)
