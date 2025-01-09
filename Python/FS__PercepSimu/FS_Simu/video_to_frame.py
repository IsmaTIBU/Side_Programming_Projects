import cv2
import os

def extraer_frames(video_path, output_folder):
    # Asegurarse de que la carpeta de salida exista
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Leer el video
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Error: No se pudo abrir el video.")
        return

    frame_count = 0
    while True:
        ret, frame = video.read()  # Leer frame por frame
        if not ret:
            break  # Si no hay más frames, salir del bucle

        # Guardar el frame como imagen
        frame_name = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_name, frame)
        frame_count += 1

    video.release()
    print(f"Frames extraídos: {frame_count}. Guardados en la carpeta '{output_folder}'.")

# Uso del script
video_path = "C:/Users/01ism/OneDrive/Desktop/red_ball.mp4"  # Cambia esto por la ruta al video
output_folder = "C:/Users/01ism/OneDrive/Desktop/Programas/Python/FS__PercepSimu/FS_Simu/Data"         # Carpeta donde se guardarán los frames
extraer_frames(video_path, output_folder)
