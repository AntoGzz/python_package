# Archivo para inicializar los objetos e importarlos sin necesidad 
# de llamar al modulo en especifico desde el main.py
# Todo lo que tenga que ver con el sistema va aqui

# Para evitar confusiones y ser mas explicito
from package_cf.workshops import unreleased
from package_cf.workshops import pokemonApi
from package_cf.workshops import dogsList

# Para proyectos que no expongan la comunidad
# from .workshops import unreleased

# print('Hola, nos encontramos en un paquete.')