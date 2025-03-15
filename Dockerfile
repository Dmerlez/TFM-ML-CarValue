# Usar una imagen oficial de Python
FROM python:3.9-slim

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de requirements.txt
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código al contenedor
COPY . .

# Comando por defecto al iniciar el contenedor
CMD ["bash"]
