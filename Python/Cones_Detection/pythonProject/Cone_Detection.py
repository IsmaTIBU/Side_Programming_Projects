import torch
from torchvision.models.detection import ssdlite320_mobilenet_v3_large, SSDLite320_MobileNet_V3_Large_Weights
from torchvision.transforms import functional as F
from PIL import Image
import matplotlib.pyplot as plt


def detect_image(model, image_path):
    model.eval()
    image = Image.open(image_path).convert("RGB")
    original_size = image.size  # Tamaño original de la imagen
    image_tensor = F.to_tensor(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image_tensor)

    # Verificar que se hayan generado predicciones
    if len(outputs) == 0 or len(outputs[0]['boxes']) == 0:
        print("No se detectaron objetos.")
        return

    boxes = outputs[0]['boxes']
    labels = outputs[0]['labels']
    scores = outputs[0]['scores']

    print(f"Se detectaron {len(boxes)} objetos")

    # Mostrar la imagen con los resultados
    plt.figure(figsize=(10, 8))
    plt.imshow(image)
    ax = plt.gca()

    # Colores para los recuadros
    color_map = {1: 'red', 2: 'green'}  # Rojo para azul, verde para amarillo

    # Dibujar los recuadros en todos los objetos detectados con un puntaje mayor al 70%
    for box, label, score in zip(boxes, labels, scores):
        if score > 0.2:  # Mostrar solo objetos con probabilidad mayor al 70%
            print(f"Etiqueta: {label.item()}, Puntaje: {score:.2f}")
            x1, y1, x2, y2 = box

            # Dibujar el recuadro
            color = color_map.get(label.item(), 'blue')
            ax.add_patch(plt.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=False, color=color, linewidth=2))

            # Determinar el texto a mostrar
            label_text = "Cône bleu" if label.item() == 1 else "Cône jaune"

            # Mostrar la probabilidad junto con el nombre del objeto
            probabilidad_texto = f"{label_text}: {score:.2}"
            ax.text(x1, y1 - 10, probabilidad_texto, color=color, fontsize=12, weight='bold')

    plt.axis('off')
    plt.show()

#SSD
# Cargar el modelo correctamente con el nuevo enfoque
weights = SSDLite320_MobileNet_V3_Large_Weights.COCO_V1
model = ssdlite320_mobilenet_v3_large(weights=weights)
model.head.classification_head.num_classes = 3

# Cargar los pesos entrenados (usa strict=False para evitar errores de tamaño)
checkpoint = torch.load("ssd_cones.pth", weights_only=True)
model.load_state_dict(checkpoint, strict=False)

# Realizar detección en una imagen de prueba
detect_image(model,
             r"C:\Users\01ism\OneDrive\Desktop\Programas\Python\Cones_Detection\FSAI-11-03-2024.v1i.coco\test\IM.jpg")
