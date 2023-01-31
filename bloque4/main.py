import subprocess
import time

def call(comando):
    subprocess.call([comando], shell=True)


# Iniciamos un clusetr de Kubernetes con 5 nodos
call("minikube start --driver=docker -p pc2 --nodes 5")

# Cambiamos al perfil que acabamos de crear
call("minikube profile pc2")

# Desplegamos los servicios y deployments
call("kubectl apply -f .")

# Esperamos hasta que todos los pods se hayan iniciado
while (str(subprocess.check_output(["kubectl get pods"])).count("Running") < 9):
    time.sleep(1)

# Abrimos la web de product-page
call("minikube service product-page")
