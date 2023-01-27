from subprocess import call

# Copiamos la carpeta de la práctica creativa 2 usada por los dockerfile
# call (["git clone https://github.com/smouuuuuk/practica_creativa2.git"], shell=True)

# Creamos las imágenes
print("Creando las imágenes...")
call (["docker build -t g38/product-page -f ./product-page/Dockerfile ."], shell=True)
call (["docker build -t g38/details -f ./details/Dockerfile ."], shell=True)
call (["docker build -t g38/ratings -f ./ratings/Dockerfile ."], shell=True)
call (["docker build -t g38/reviews-v1 -f ./reviews/Dockerfile --build-arg service_version=v1 --build-arg enable_ratings=false --build-arg star_color=black ."], shell=True)
call (["docker build -t g38/reviews-v2 -f ./reviews/Dockerfile --build-arg service_version=v2 --build-arg enable_ratings=true --build-arg star_color=black ."], shell=True)
call (["docker build -t g38/reviews-v3 -f ./reviews/Dockerfile --build-arg service_version=v3 --build-arg enable_ratings=true --build-arg star_color=red ."], shell=True)
print("Imágenes creadas")

# Una vez creadas las imágenes podemos eliminar la carpeta
# call (["rm -rf ./practica_creativa2"], shell=True)

# Lanzamos el docker-compose
print("Lanzando los contenedores...")
call(["docker compose up"], shell=True)

