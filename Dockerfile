FROM python:3.8

# Instala las dependencias necesarias
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install fastai --upgrade

ENV PYTHONPATH $PYTHONPATH:/usr/local/lib/python3.8/site-packages/fastai

WORKDIR /app

# Copia el código de la API y el modelo al contenedor
COPY app.py .
COPY model.pkl .

# Establece el puerto y el comando para ejecutar la API
EXPOSE 8080
CMD ["python", "/app/app.py"]
