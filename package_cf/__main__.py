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
from package_cf import unreleased
from package_cf import pokemonApi
from package_cf import dogsList

if __name__ == '__main__':
# Manera tipica de definir un msg
# print('>>> Iniciando ejecución de unreleased')

# Manera correcta utilizando la libreria logging
    logging.debug('>>> Iniciando ejecución de unreleased')
    workshops = unreleased()
    logging.debug(workshops)
    logging.debug('>>> Finalizando ejecución')

    logging.debug('>>> Iniciando ejecución de pokemonApi')
    pokemon_stats = pokemonApi()
    logging.debug(pokemon_stats)
    logging.debug('>>> Finalizando ejecución')

    logging.debug('>>> Iniciando ejecución de dogsList')
    dogs_list = dogsList()
    logging.debug(dogs_list)
    logging.debug('>>> Finalizando ejecución')

    # Test
    # print('Taller de Python')