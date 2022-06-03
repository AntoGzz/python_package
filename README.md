# README.md
    Paquete para el API de la plataforma.

# 1. Iniciar entorno virtual
py -m venv env ó python -m venv env

# 2. Activar el entorno virtual 
source env/Scripts/activate

# 3. Instalar la libreria Request en el entorno virtual
python -m pip install requests

# 4. Listar dependencias del entorno y actualizar el requirements.txt
pip freeze > requirements.txt

# 5. Iniciar ejecución del paquete
python -m package_cf

# 6. Preparar el setup para desplegar el paquete
python setup.py sdist

# 7. Instalar twine (nos permite autenticarnos con pip en el deploy), si aparece un error hacerle un upgrade a pip "pip install pip --upgrade"
python -m pip install twine

# 8. Desplegar el paquete, nos pedira el username y el password. Luego podemos probarlo usando la ruta que nos da
twine upload dist/*

# 9. Testear el paquete desplegado
pip install package_name

# 10. Si se instala satisfactoriamente, podemos entrar al interprete de python e importar la libreria
pyhton
from package_name import dogsList
dogsList()

