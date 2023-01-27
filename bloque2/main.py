from subprocess import call

call (["git clone https://github.com/smouuuuuk/practica_creativa2.git"], shell=True)
call (["docker build -t g38/product-page:mono ."], shell=True)
call (["rm -rf ./practica_creativa2"], shell=True)
call (["docker run --rm -it --name g38-product-page -p 9080:9080 g38/product-page:mono"], shell=True)
