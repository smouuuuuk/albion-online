import subprocess

def call(comando):
    subprocess.call([comando], shell=True)

call (["git clone https://github.com/smouuuuuk/practica_creativa2.git"])
call (["docker build -t g38/product-page:mono ."])
call (["rm -rf ./practica_creativa2"])
call (["docker run --rm -it --name g38-product-page -p 9080:9080 g38/product-page:mono"])
