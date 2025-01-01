# Usar la imagen base de Python
FROM python:3.9-slim

# Instalar las dependencias del sistema necesarias para Pillow
RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libjpeg-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Actualizar pip antes de instalar dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación al contenedor
COPY app/ /app/

# Exponer el puerto 5000
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]

