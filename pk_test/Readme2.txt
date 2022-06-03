Crea tu primer paquete Open Source con Python
En esta guía aprenderás cómo crear tus paquetes Open source utilizando Python y subirlo a los repositorios de PyPI.

Para fines prácticos, la guía tiene como objetivo crear un CLI con Python capas de consumir los diferentes endpoints del API oficial de CódigoFacilito. 🐊

REQUERIMIENTOS. 🕵️‍♀️
Para poder seguir esta guía, será necesario cuentes con los siguientes requerimientos.

Cuenta activa en Github.
Cuenta activa en PyPI.
Conocimientos básicos de Python.
Alcance de tu proyecto.
Nombre de tu proyecto.
ALCANCE DEL PROYECTO
El primer paso, y quizás el más difícil, es sin duda alguna identificar el alcance que tendrá nuestro proyecto.

Sé que desde un principio queremos liberar un proyecto 100% "terminado", que cumpla con todos los requerimientos que hemos planteado y solvente todas las problemáticas expuestas. Sin embargo, desarrollar un software con estas características es algo costoso, tanto en tiempo como financieramente. 😱

Por lo tanto te recomiendo versiones tu proyecto; de esta forma, con cada nueva versión liberada, podrás ir iterando sobre el proyecto, resolviendo bugs y añadiendo nuevas funcionalidades.

Esto no solo te permitirá escuchar las necesidades de tus usuarios, si no además, te permitirá definir nuevos objetivos a cumplir. Objetivos que quizás no hayas planteado en primera instancias.

Recuerda, Roma no se construyo en un día. No importa si tu proyecto se encuentra "terminado" en la versión 2 o en la versión 1024. 😎

NOMBRE DEL PROYECTO
A diferencia de lo que muchos podemos llegar a pensar, el nombre de nuestro proyecto es fundamental para su éxito.

Sí queremos que el proyecto sea usados por miles de desarrolladores(as) al rededor del mundo, debemos asegurarnos que el nombre sea fácil de recordar.

Te recomiendo utilizar nombres cortos y concisos. Esto te puede asegurar un mayor alcance en el motor de búsqueda de PyPI.

Si quieres conocer si el nombre que estas pensando aun se encuentra disponible, recuerda que siempre puedes buscarlo en el sitio oficial de PyPI.

ESTRUCTURA
Una vez definido el alcance y el nombre del proyecto, lo siguiente que debemos hacer será comenzar con el proceso de desarrollo.

Te recomiendo utilicemos la siguiente estructura para tu proyecto.

root/
│
├── env/
├── <Paquete>/
│   ├── __init__.py
│   ├── __main__.py
│
├── tests/
│   ├── test.py
│
├── README.md
├── .gitignore
├── requirements.txt
└── main.py
Es una estructura básica, pero sumamente eficiente. 🤠

Tú deberás colocar el nombre que desees para tu paquete.

PREPARACIÓN DEL PROYECTO
Lo primero será crear nuestro entorno virtual. Para ello ejecutamos el siguiente comando en consola.

python -m venv env
Esto creará la carpeta env dentro del directorio.

Una vez con la carpeta creada, lo siguiente será activar el entorno.

Windows.

env\Scripts\activate
Linux.

source env/bin/activate
Una vez el entorno se encuentre activado ya podremos instalar todas las dependencias que nuestro proyecto necesite.

Para este tutorial será necesario instalar la librería de requests.

pip install requests
Siempre que instalemos o desinstalemos alguna dependencia, será necesario registrar estos cambios en el archivo requirements.txt,.

pip freeze > requirements.txt
Para evitar que archivos innecesarios se alojen en el repositorio, debemos configurar el archivo .gitignore. Te recomiendo utilices el archivo gitignore que hemos creado en CódigoFacilito.

Para el archivo README.md debemos detallar el funcionamiento de nuestro paquete. Este archivo servirá como la documentación del proyecto. 😎

Te recomiendo ampliamente te tomes el tiempo necesario para este archivo. Entre más detallada se encuentre la documentación, será más sencillo para nuestros usuarios poder implementar nuestro software.

Si el tema de la documentación supone un reto para ti, te recomiendo el curso


Fundamentos de escritura para prog...

88%

Equipo Código Facilito

1h 19m
Ir al curso
" target="_blank">Fundamentos de escritura para programadores. En este curso te enseñamos cómo utilizar Markdown y como redactar de mejor manera.
Listo, una vez con lo archivos básicos configurados, ya podemos alojar nuestro proyecto en el repositorio de Git. Aquí un tutorial de cómo hacerlo.

DESARROLLO
Lo siguiente que debemos hacer será comenzar con el desarrollo. Toda nuestra lógica de programación (Variables, constantes, funciones, clases, métodos, etc... ) Deberás encontrarse dentro del paquete.

En mi caso, he creado el archivo workshops.py, que será uno de los módulos de mi paquete.

├── <Paquete>/
│   ├── __init__.py
│   ├── __main__.py
│   ├── workshops.py
Este archivo tiene la finalidad de poder consumir todos los EndPoints relacionados con talleres.

workshops.py.

import requests

def unreleased():
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')

    if response.status_code == 200:
        payload = response.json() 
        return payload['data']
Para exponer la funcionalidad de nuestro módulo lo haremos a través del archivo __init__.

from codigofacilito.workshops import unreleased
Una vez con el import realizado debemos testear el paquete utilizando el archivo __main__.

Aquí un ejemplo de cómo hacerlo.

import logging

from codigofacilito import unreleased

logging.basicConfig(level=logging.INFO)

def main():
    logging.info(unreleased())


if __name__ == '__main__':
    logging.debug('>>> Estamos comenzando la ejecución del paquete.')

    main()

    logging.debug('>>> Estamos finalizando la ejecución del paquete.')
En consola ejecutaremos el siguiente comando.

python -m <El nombre de nuestro paquete>
Si todo ha salido bien deberíamos visualizar en consola la respuesta por parte del servidor (Para mi ejemplo el listado de próximos talleres).

Recuerda mantener actualizado tu repositorio Git en todo momento. Commits pequeños para cada nueva funcionalidad estarán bastante bien. 🤖

ARCHIVOS DE CONFIGURACIÓN
Una vez hayamos confirmado que nuestro paquete funciona adecuadamente, lo siguiente será preparar el proyecto para su despliegue.

Para ello vamos a crear 2 nuevos archivos.

setup.py
LICENSE.txt.
Para el archivo setup.py te recomiendo copies y pegues la siguiente estructura. Deberás definir tus propios valores para las constantes.

from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Description'
PACKAGE_NAME = 'Package Name'
AUTHOR = ''
EMAIL = ''
GITHUB_URL = ''

setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
Y para el archivo LICENSE.txt, deberás colocar la licencia que desees tu proyecto posea.

En mi caso estaré utilizando la licencia MIT, que podrás encontrar en el repositorio de CódigoFacilito.

DESPLIEGUE
El archivo setup.py tiene como finalidad poder configurar nuestro proyecto para su release. Por lo tanto, una vez hayamos creado y configurado los archivos setup.py y LICENSE.txt, lo siguiente será crear un archivo con extensión .tar.gz. Para ello ejecutamos el siguiente comando.

python setup.py sdist
Esto va a crear la carpeta dist dentro del directorio. Será dentro de esta carpeta donde se encontrará el archivo .tar.gz. El archivo seguirá la siguiente estructura por nombre.

<Nombre del paquete>-<version>.tar.gz
Este será el archivo que debemos subir al repositorio de PyPI. 🙌

Ahora, vamos a instalar la librería twine.

Primero actualizamos pip.

pip install pip --upgrade
Instalamos twine.

pip install twine
Para hacer el despliegue ejecutamos el siguiente comando.

twine upload dist/*
Este comando nos pedirá el username y password de nuestra cuenta PyPI.

Si todo ha salido bien, deberíamos ver en consola el link del proyecto en PyPI, listo para ser utilizando por la comunidad Python. 🤠

NUEVAS VERSIONES 🔥
Para finalizar la guía aprenderemos a actualizar nuestro proyecto.

Recordemos que ahora nuestro proyecto se encuentra versionado. Esto lo hemos definido mediante la constante VERSION del archivo setup.py. Por lo tanto, para poder liberar una nueva versión del proyecto debemos modificar esta constate.

Las versiones siempre son auto incrementales en 1, así que te invito mantengas la convención.

Pasar de la versión 0.0.1 a al versión 0.0.10 (Por ejemplo) puede causar problemas en el despliegue.

Para mi segunda versión lo que haré será implementar el CLI.

En el archivo setup.py añadimos una nueva entrada: entry_points.

VERSION = '0.0.2'

setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    entry_points={
        "console_scripts":
            ["pycody=codigofacilito.__main__:main"]
    },
    version = VERSION,
    ...
Para este ejemplo le indico a Python que, cuando el comando pycody se ejecute en terminal se hará el llamado de la función main que se encuentra en el archivo __main__ del paquete codigofacilito. Recordemos que esta función permite mostrar en consola todos los talleres próximos en la plataforma.

Lo que resta por hacer será generar el nuevo archivo .tar.gz y subirlo a los servidores. 🌈

python setup.py sdist
twine upload dist/*