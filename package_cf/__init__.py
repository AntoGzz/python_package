# Archivo para inicializar los objetos e importarlos sin necesidad 
# de llamar al modulo en especifico desde el main.py

# Para evitar confusiones y ser mas explicito
from package_cf.workshops import unreleased
from package_cf.workshops import pokemonApi

# Para proyectos que no expongan la comunidad
# from .workshops import unreleased

# print('Hola, nos encontramos en un paquete.')