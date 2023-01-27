from subprocess import call, check_output
import time

#Necesario tener helm instalado

# Necesitamos primero iniciar un cluster de Kubernetes
call(["minikube start --driver=docker -p pc2 --nodes 5"], shell=True)

# Cambiamos al perfil que acabamos de crear
call(["minikube profile pc2"], shell=True)

# Desplegamos helm sobre el cluster creado
call(["helm install pc2 ."], shell=True)

# Esperamos hasta que todos los pods se hayan iniciado
while (str(check_output(["kubectl get pods"], shell=True)).count("Running") < 9):
    time.sleep(1)

# Exponemos el puerto 9080 de la product-page
call(["kubectl expose deployment product-page-latest --type=NodePort --port=9080"], shell=True)

# Abrimos la web de product-page
call(["minikube service product-page-latest"], shell=True)