import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__, template_folder=os.path.abspath("templates"))

@app.route("/")
def home():
    return render_template("index.html")

# Cargar el modelo
MODEL_PATH = "models/car_value_model.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# Carpeta para subir imágenes
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Preprocesamiento de la imagen
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((224, 224))  # Ajusta según el modelo
    img = np.array(img) / 255.0   # Normalizar valores
    img = np.expand_dims(img, axis=0)  # Añadir dimensión batch
    return img

@app.route("/", methods=["GET", "POST"])
def upload_and_predict():
    if request.method == "POST":
        # Obtener archivo subido
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)  # Guardar imagen

            # Preprocesar la imagen
            img = preprocess_image(file_path)

            # Hacer predicción
            prediction = model.predict(img)
            predicted_value = prediction[0][0]
            predicted_value = (predicted_value * 10000).round(2) 


            return render_template("index.html", image=filename, prediction=predicted_value)

    return render_template("index.html", image=None, prediction=None) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
