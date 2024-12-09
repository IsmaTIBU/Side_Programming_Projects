import torch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as T
from pycocotools.coco import COCO
import cv2
import os



class COCODataset(Dataset):
    def __init__(self, root_dir, annotation_file, transforms=None, max_images=None):
        self.root_dir = root_dir
        self.coco = COCO(annotation_file)
        self.transforms = transforms
        self.ids = list(self.coco.imgs.keys())

        # Limitar la cantidad de imágenes si se especifica max_images
        if max_images is not None:
            self.ids = self.ids[:max_images]

    def __getitem__(self, index):
        coco = self.coco
        img_id = self.ids[index]
        ann_ids = coco.getAnnIds(imgIds=img_id)
        anns = coco.loadAnns(ann_ids)

        # Cargar imagen
        img_info = coco.loadImgs(img_id)[0]
        img_path = os.path.join(self.root_dir, img_info['file_name'])

        if not os.path.exists(img_path):
            raise FileNotFoundError(f"No se pudo encontrar la imagen: {img_path}")

        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Obtener bounding boxes y etiquetas
        boxes = []
        labels = []
        for ann in anns:
            x, y, width, height = ann['bbox']
            boxes.append([x, y, x + width, y + height])
            labels.append(ann['category_id'])

        boxes = torch.tensor(boxes, dtype=torch.float32)
        labels = torch.tensor(labels, dtype=torch.int64)
        target = {"boxes": boxes, "labels": labels}

        if self.transforms:
            image = self.transforms(image)

        return image, target

    def __len__(self):
        return len(self.ids)


def get_transforms():
    return T.Compose([T.ToTensor()])
