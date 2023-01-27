# Partimos de ruby:2.7.1-slim como imagen base
FROM ruby:2.7.1-slim

# Definimos la variable de entorno ENABLE_EXTERNAL_BOOK_SERVICE             
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

# Copiamos el fichero details.rb a /opt/microservices
COPY practica_creativa2/bookinfo/src/details/details.rb /opt/microservices/details.rb

# Exponemos el puerto 9080 del contenedor
EXPOSE 9080

# Lanzamos la aplicación en el puerto correspondiente en el arranque del contenedor
CMD ruby /opt/microservices/details.rb 9080

# Para crear la imagen:
# docker build -t g38/details -f ./details/Dockerfile .