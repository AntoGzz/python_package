# Instructivo de instalación
    Paquete para el API de la plataforma.

###### 1. Iniciar entorno virtual
`py -m venv env ó python -m venv env`

###### 2. Activar el entorno virtual 
`source env/Scripts/activate`

###### 3. Instalar la libreria Request en el entorno virtual
`python -m pip install requests`

###### 4. Listar dependencias del entorno y actualizar el requirements.txt
`pip freeze > requirements.txt`

###### 5. Iniciar ejecución del paquete
`python -m package_name`

###### 6. Preparar el setup para desplegar el paquete
`python setup.py sdist`

###### 7. Instalar twine (nos permite autenticarnos con pip en el deploy), si aparece un error hacerle un upgrade a pip "pip install pip --upgrade"
`python -m pip install twine`

###### 8. Desplegar el paquete, nos pedira el username y el password. Luego podemos probarlo usando la ruta que nos da
`twine upload dist/*`
###### 8.1 En caso de que falle el comando superior, ejecutar
`python -m twine upload dist/*`

###### 9. Testear el paquete desplegado
`pip install package_name`

###### 10. Si se instala satisfactoriamente, podemos entrar al interprete de python e importar la libreria
```
python
from package_name import dogsList
dogsList()
```

![image](https://user-images.githubusercontent.com/23372415/171760844-754c23b8-484f-460b-95b6-fa62b1eb349b.png)

## 11. Crear el CLI para en vez de utilizar el interprete, utilicemos un comando y ya se ejecute la funcion del paquete
###### 11.0 Definimos los entry_points para definir los comandos de ejecución, reconstruimos el dist con el paso 6 y luego resubir con el paso 8
###### 11.1 Upgradeamos el paquete en su nueva version
`pip install package_name --upgrade`

###### 12. Ahora ya podemos ejecutar el comando que definimos y nos mostrara nuestra ejecución

###### 13. Actualizamos el requirements.txt
`pip freeze > requirements.txt`