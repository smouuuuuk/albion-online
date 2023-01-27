# Partimos de python:3.7 como imagen base
FROM python:3.7

# Copiamos el directorio productpage al contenedor
COPY ./practica_creativa2/bookinfo/src/productpage ./productpage

# Definimos la variable de entorno GROUP_NUMBER
ENV GROUP_NUMBER=38

# Nos movemos al directorio correspondiente
WORKDIR productpage

# Instalamos las dependencias (habiendo eliminado previamente los requerimientos estrictos de versión de urllib3 y requests)
RUN python3 -m pip install -r requirements.txt

# Lanzamos la aplicación en el puerto correspondiente en el arranque del contenedor
CMD python3 ./productpage_monolith.py 9080

# Para crear la imagen:
# docker build -t g38/product-page:mono .

# Para lanzar el contenedor:
# docker run --rm -it --name g38-product-page -p 9080:9080 g38/product-page:mono
