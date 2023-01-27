FROM websphere-liberty:20.0.0.6-full-java8-ibmjava

ENV SERVERDIRNAME reviews

# Únicamente modificamos la primera parte de esta línea para referenciar al directorio correcto
COPY ./practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg/servers/LibertyProjectServer /opt/ibm/wlp/usr/servers/defaultServer/

RUN /opt/ibm/wlp/bin/installUtility install  --acceptLicense /opt/ibm/wlp/usr/servers/defaultServer/server.xml && \
    chmod -R g=rwx /opt/ibm/wlp/output/defaultServer/

ARG service_version
ARG enable_ratings 
ARG star_color
ENV SERVICE_VERSION ${service_version}
ENV ENABLE_RATINGS ${enable_ratings}
ENV STAR_COLOR ${star_color}

CMD ["/opt/ibm/wlp/bin/server", "run", "defaultServer"]

# Para crear la imagen (cambiando los valores "service_version" y "star_color" según la versión):
# docker build -t g38/reviews-v1 -f ./reviews/Dockerfile --build-arg service_version=v1 --build-arg enable_ratings=false --build-arg star_color=black .
