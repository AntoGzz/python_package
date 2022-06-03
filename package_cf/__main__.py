# Archivo para ejecutar utilizando el interprete de python sin necesidad del main.py

# Importamos el modulo de msg
import logging # Por defecto los msg de tipo warning o superior seran vistos

"""
INFO -> 10
DEBUG -> 20
WARNING -> 30
ERROR -> 40
CRITICAL -> 50
"""

# Para definir que los msg de menor nivel se vean, se debe colocar
logging.basicConfig(level=logging.DEBUG)

# Importamos las funciones del paquete
from package_cf import unreleased, workshops
from package_cf import pokemonApi
from package_cf import dogsList

# Definimos main despues de los entry_points
def main():
    workshops = unreleased()
    logging.info(workshops)
    # Tambien podriamos colocarlo como 
    # logging.info(unreleased())

if __name__ == '__main__':
# Manera tipica de definir un msg
# print('>>> Iniciando ejecución de unreleased')

# Manera correcta utilizando la libreria logging
    logging.debug('>>> Iniciando ejecución de unreleased')
    
    # Añadiendo esto podemos imprimir el doc string para testearlo
    logging.debug(help(unreleased.__doc__))

    # Despues de los entry_points
    main()

    logging.debug('>>> Finalizando ejecución')

    # Test
    # print('Taller de Python')