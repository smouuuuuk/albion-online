#Google Cloud (FALTA dirección IP Pública)

#Importamos las librerías necesarias:
import sys
import json
import time
from subprocess import call

call(["echo 'y' | sudo apt-get update"], shell=True)
call(["echo 'y' | sudo apt install python3-pip"], shell=True)
call(["git clone https://github.com/CDPS-ETSIT/practica_creativa2.git"], shell=True) #Descargamos los archivos almacenados en el directorio de GitHub de la práctica
call(["pip3 install urllib3"], shell=True)
call(["pip3 install flask_bootstrap"], shell=True)
call(["pip3 install chardet"], shell=True)
call(["pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt"], shell=True) #Instalamos las dependencias especificadas en el fichero requirements.txt usando pip(3)
call(["pip3 install --upgrade requests"], shell=True)
call(["echo 'y' | sudo apt-get update"], shell=True)

fin = open("practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", 'r') # Fichero de entrada necesario para ejecutar la aplicación
fout = open("practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py", 'w') # Fichero de salida
for line in fin:
  if "reviewsHostname = "+r'"'+"reviews"+r'"'+" if (os.environ.get("+r'"'+"REVIEWS_HOSTNAME"+r'"'+") is None) else os.environ.get("+r'"'+"REVIEWS_HOSTNAME"+r'"'+")" in line :
   fout.write(line+ "\nos.environ['GROUP_NUMBER']="+r'"'+"Grupo 38"+r'"'+" \n") 
  elif "'title': 'The Comedy of Errors'," in line :
    fout.write("'title': 'The Comedy of Errors ' +os.environ['GROUP_NUMBER'],")
  elif "'author': book['authors'][0]," in line :
    fout.write(line + "        'grupo' : os.environ['GROUP_NUMBER'],\n")
  else:
   fout.write(line)
fin.close()
fout.close()
               
call(["sudo","cp","practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py","practica_creativa2/bookinfo/src/productpage/productpage_monolith.py"])
call(["sudo","rm","practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py"])
                           
fin = open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", 'r') 
fout = open("practica_creativa2/bookinfo/src/productpage/templates/productpage2.html", 'w') 
for line in fin:
  if "{% block title %}Simple Bookstore App{% endblock %}" in line :
   fout.write("{% block title %}Simple Bookstore App {{ details.grupo }}{% endblock %}")
  else:
   fout.write(line)
fin.close()
fout.close()

call(["sudo","cp","practica_creativa2/bookinfo/src/productpage/templates/productpage2.html","practica_creativa2/bookinfo/src/productpage/templates/productpage.html"])
call(["sudo","rm","practica_creativa2/bookinfo/src/productpage/templates/productpage2.html"])

call(["sudo python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080"], shell=True)
#9080 es el puerto en el que queremos que la aplicación reciba las peticiones
