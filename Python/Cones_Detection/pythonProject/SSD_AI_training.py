import torch
from torch.utils.data import DataLoader
from torchvision.models.detection import ssdlite320_mobilenet_v3_large
from tqdm import tqdm
import matplotlib.pyplot as plt
from SSD_Dataset_setting import COCODataset, get_transforms

def train_ssd(model, data_loader, device, patience=3):
    model.to(device)
    model.train()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.005, momentum=0.9)

    # Lista para almacenar la pérdida por cada época
    epoch_losses = []
    best_loss = float('inf')
    patience_counter = 0
    epoch = 0
    initial_loss = None

    # Entrenamiento hasta que la pérdida sea menor a una décima parte del primer epoch loss
    while True:
        total_loss = 0
        for images, targets in tqdm(data_loader, desc=f"Epoch {epoch + 1}"):
            images = [img.to(device) for img in images]
            targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

            # Calcular la pérdida
            loss_dict = model(images, targets)
            losses = sum(loss for loss in loss_dict.values())

            optimizer.zero_grad()
            losses.backward()
            optimizer.step()

            total_loss += losses.item()

        # Almacenar la pérdida total de la época
        epoch_losses.append(total_loss)
        print(f"Epoch {epoch + 1} Loss: {total_loss:.4f}")

        # Guardar la pérdida inicial
        if epoch == 0:
            initial_loss = total_loss

        # Verificar si la pérdida actual es menor o igual a una décima parte de la pérdida inicial
        if initial_loss is not None and total_loss <= initial_loss / 10:
            print(f"Entrenamiento detenido: la pérdida ({total_loss:.4f}) es menor o igual a una décima parte de la pérdida inicial ({initial_loss:.4f}).")
            break

        # Verificar si la pérdida ha mejorado para early stopping
        if total_loss < best_loss:
            best_loss = total_loss
            patience_counter = 0
            torch.save(model.state_dict(), "best_model.pth")
            print("Mejora en la pérdida. Modelo guardado.")
        else:
            patience_counter += 1
            print(f"No hay mejora. Paciencia: {patience_counter}/{patience}")

        # Detener si no hay mejora durante 'patience' épocas
        if patience_counter >= patience:
            print("Early stopping activado.")
            break

        epoch += 1

    # Mostrar el gráfico de pérdida al final del entrenamiento
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(epoch_losses) + 1), epoch_losses, marker='o', linestyle='-', color='b')
    plt.title("Pérdida por Época")
    plt.xlabel("Época")
    plt.ylabel("Pérdida")
    plt.grid(True)
    plt.show()

    return epoch_losses


# Ajustar las rutas para tu dataset
root_dir = r"C:/Users/01ism/OneDrive/Desktop/Programas/Python/Cones_Detection/FSAI-11-03-2024.v1i.coco/train"
annotation_file = r"C:/Users/01ism/OneDrive/Desktop/Programas/Python/Cones_Detection/FSAI-11-03-2024.v1i.coco/train/_annotations.coco.json"

# Establecer el límite de imágenes con max_images
dataset = COCODataset(root_dir, annotation_file, transforms=get_transforms(), max_images=30)
data_loader = DataLoader(dataset, batch_size=4, shuffle=True, collate_fn=lambda x: tuple(zip(*x)))

# Crear y entrenar el modelo
model = ssdlite320_mobilenet_v3_large(weights=True)
model.head.classification_head.num_classes = 3

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Entrenar el modelo en función de la condición de convergencia
epoch_losses = train_ssd(model, data_loader, device, patience=3)

# Guardar el modelo final
torch.save(model.state_dict(), "ssd_cones_final.pth")