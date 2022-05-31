import requests

def unreleased():
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')

    if response.status_code == 200:
        payload = response.json()
        return payload['data']

def pokemonApi():
    response = requests.get('https://pokeapi.co/api/v2/pokemon/charmander')

    if response.status_code == 200:
        payload = response.json()
        return payload['stats']