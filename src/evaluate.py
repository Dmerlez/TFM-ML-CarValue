import tensorflow as tf

# Cargar modelo en el nuevo formato
model = tf.keras.models.load_model("models/car_value_model.keras")

print("Modelo cargado exitosamente")
