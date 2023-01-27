# Práctica Creativa 2 - Grupo 38

Repositorio de github con todo el código desarrollado para la práctica.

## Partes

Está compuesto por los 4 bloques principales de la práctica:
* **bloque1**: Despliegue de la aplicación en máquina virtual pesada
* **bloque2**: Despliegue de una aplicación monolítica usando docker
* **bloque3**: Segmentación de una aplicación monolítica en microservicios utilizando docker-compose
* **bloque4**: Despliegue de una aplicación basada en microservicios utilizando Kubernetes
* **helm-charts**: Desplegar usando Helm Charts toda la infraestructura de la práctica

## Ejecución

### Bloque1

Utilizaremos Google Cloud, crearemos una instancia de MV con Ubuntu como OS. Una vez creada entraremos a ella a través de SSH en el navegador y subiremos nuestro script de python (_pyGoogleCloud.py_). Podemos pasar a ejecutar el archivo con:
```bash
python3 ./pyGoogleCloud.py
```
Para poder acceder a la web utilizando la IP externa de la máquina debemos primero crear una regla de firewall que nos permita llegar al puerto que estemos utilizando en nuestro proyecto para servir la web, en nuestro caso es el puerto 9080. Crearemos una regla con los siguientes parámetros:

![image](https://user-images.githubusercontent.com/94694675/215090450-277536b6-6b1c-4cb5-a305-ebe0a6e46e02.png)

Una vez creado la regla podremos acceder a `http://external-IP:9080` y podremos ver nuestra web.

### Resto de bloques

Para ejecutar el resto de bloques cada uno de ellos viene con un script _main.py_ incluido, por lo tanto para ejecutar cada parte debemos situarnos dentro del directorio correspondiente y usar el siguiente comando:
```bash
python3 ./main.py
```
El script se encargará de lanzar los comandos necesarios para iniciar cada uno de los bloques correspondientes.

Es importante recalcar que para que funcione correctamente el script hace falta tener las dependencias necesarias instaladas. Debemos tener las siguientes instaladas en el dispositivo para poder ejecutar correctamente todos los escenarios.
* **docker** - necesario que tenga la opción **compose**
* **minikube**
* **kubectl**
* **helm**
