# Partimos de node:12.18.1-slim como imagen base
FROM node:12.18.1-slim

# Copiamos todos los ficheros de del directorio ratings a /opt/microservices
COPY ./practica_creativa2/bookinfo/src/ratings/* /opt/microservices/

# Definimos la variable de entorno SERVICE_VERSION
ENV SERVICE_VERSION=v1

# Nos movemos al directorio correspondiente
WORKDIR /opt/microservices

# Actualizamos las dependencias indicadas en package.json
RUN npm install

# Exponemos el puerto 9080 del contenedor
EXPOSE 9080

# Lanzamos la aplicación en el puerto correspondiente en el arranque del contenedor
CMD node ratings.js 9080

# Para crear la imagen:
# docker build -t g38/ratings -f ./ratings/Dockerfile .
