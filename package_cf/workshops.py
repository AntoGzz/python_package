import requests

def unreleased():
    # Doc string es un comentario en la 1ra linea de la funcion para testear
    """Retorna los proximos talleres de código facilito.
    >>> type(unreleased()) == type(dict())
    True
    """

    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')

    if response.status_code == 200:
        payload = response.json()
        # Imprimir el tipo de objeto
        # print(type(payload['data']))
        return payload['data']

def pokemonApi():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')

    if response.status_code == 200:
        payload = response.json()
        return payload['stats']

def dogsList():
    response = requests.get('https://dog.ceo/api/breeds/list/all')

    if response.status_code == 200:
        payload = response.json()
        return payload['message']