import os
from PIL import Image
import numpy as np
from tensorflow.keras.Model import Model
from tensorflow.keras.layers import Input, Dense, Flatten, Reshape
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# Función para cargar imágenes
def cargar_imagenes(carpeta):
    imagenes = []

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".jpg") or archivo.endswith(".png"):
            ruta_imagen = os.path.join(carpeta, archivo)
            imagen = Image.open(ruta_imagen).convert("RGB")
            imagen = imagen.resize((128, 128))  # Redimensionar las imágenes
            imagen_array = np.array(imagen) / 255.0  # Normalizar entre 0 y 1
            imagenes.append(imagen_array)

    return np.array(imagenes)

# Cargar las imágenes de la carpeta
carpeta = "C:/Users/01ism/OneDrive/Desktop/Programas/Python/FS__PercepSimu/FS_Simu/Data"
imagenes = cargar_imagenes(carpeta)

# Dividir los datos en entrenamiento y prueba
x_train, x_test = train_test_split(imagenes, test_size=0.2, random_state=42)

# Construir el autoencoder
input_shape = (128, 128, 3)
input_img = Input(shape=input_shape)

# Codificador
x = Flatten()(input_img)
x = Dense(256, activation="relu")(x)
encoded = Dense(128, activation="relu")(x)

# Decodificador
x = Dense(256, activation="relu")(encoded)
x = Dense(np.prod(input_shape), activation="sigmoid")(x)
decoded = Reshape(input_shape)(x)

# Modelo completo
autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer=Adam(learning_rate=0.001), loss="mse")

# Entrenar el modelo
autoencoder.fit(
    x_train, x_train,
    epochs=20,
    batch_size=32,
    validation_data=(x_test, x_test)
)

# Guardar el modelo
autoencoder.save("autoencoder_esfera_roja.h5")
print("Modelo de autoencoder guardado como 'autoencoder_esfera_roja.h5'")
