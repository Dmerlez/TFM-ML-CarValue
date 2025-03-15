# Usar una imagen oficial de Python
FROM python:3.9-slim

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt .
COPY src/ src/
COPY models/ models/
COPY templates/ templates/
COPY static/ static/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto para Flask
EXPOSE 5000

# Ejecutar la aplicación Flask
CMD ["python", "src/app.py"]
