import subprocess
import time

def call(comando):
    subprocess.call([comando], shell=True)

#Necesario tener helm instalado

# Necesitamos primero iniciar un cluster de Kubernetes
call(["minikube start --driver=docker -p pc2 --nodes 5"])

# Cambiamos al perfil que acabamos de crear
call(["minikube profile pc2"])

# Desplegamos helm sobre el cluster creado
call(["helm install pc2 ."])

# Esperamos hasta que todos los pods se hayan iniciado
while (str(subprocess.check_output(["kubectl get pods"])).count("Running") < 9):
    time.sleep(1)

# Exponemos el puerto 9080 de la product-page
call(["kubectl expose deployment product-page-latest --type=NodePort --port=9080"])

# Abrimos la web de product-page
call(["minikube service product-page-latest"])