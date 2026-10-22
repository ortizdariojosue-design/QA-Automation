import requests

def test_pikachu():
    
    respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert respuesta.status_code == 200
    

def test_id_25():
    respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert respuesta.json()["id"] == 25

def test_nombre_pikachu():
    respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert respuesta.json()["name"] == "pikachu"