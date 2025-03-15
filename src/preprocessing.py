import cv2
import os
import numpy as np

DATA_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

for img_name in os.listdir(DATA_DIR):
    img_path = os.path.join(DATA_DIR, img_name)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224, 224))  # Redimensionar a 224x224 píxeles
    img = img / 255.0  # Normalizar
    np.save(os.path.join(PROCESSED_DIR, img_name.replace(".jpg", ".npy")), img)
