import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN ='ce2bfdbb92bc1513d27b7187d9298965'
HEADER = {'Conttent-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '14931'

def test_status_code():
    response = requests.get(url =f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get=requests.get(url =f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"]== 'New Name'

def test_treners_status_cod():
    response = requests.get(url =f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_treners_of_respons():
    respons_get=requests.get(url= f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert respons_get.json()["data"][0]["trainer_name"] =="Bars"


