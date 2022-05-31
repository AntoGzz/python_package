# Archivo para ejecutar utilizando el interprete de python sin necesidad del main.py
from package_cf import unreleased
from package_cf import pokemonApi

if __name__ == '__main__':

    print('>>> Iniciando ejecución de unreleased')
    workshops = unreleased()
    print(workshops)
    print('>>> Finalizando ejecución')

    print('>>> Iniciando ejecución de pokemonApi')
    pokemon_stats = pokemonApi()
    print(pokemon_stats)
    print('>>> Finalizando ejecución')
    
    # Test
    # print('Taller de Python')