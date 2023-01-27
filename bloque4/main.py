from subprocess import call, check_output
import time

# Iniciamos un clusetr de Kubernetes con 5 nodos
call(["minikube start --driver=docker -p pc2 --nodes 5"], shell=True)

# Cambiamos al perfil que acabamos de crear
call(["minikube profile pc2"], shell=True)

# Desplegamos los servicios y deployments
call(["kubectl apply -f ."], shell=True)

# Esperamos hasta que todos los pods se hayan iniciado
while (str(check_output(["kubectl get pods"], shell=True)).count("Running") < 9):
    time.sleep(1)

# Abrimos la web de product-page
call(["minikube service product-page"], shell=True)