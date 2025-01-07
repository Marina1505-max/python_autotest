import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN ='ce2bfdbb92bc1513d27b7187d9298965'
HEADER = {'Conttent-Type' : 'application/json', 'trainer_token': TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "marina-a-d@domail.ru",
    "password": "Iloveqa11111"
}
body_confeirmation = {
    "trainer_token": TOKEN
    }
body_create = {
    "name": "generate",
    "photo_id": -1
}
body_new_name = {
    "pokemon_id": "183831",
    "name": "New Name"
}
body_pokeball= {
    "pokemon_id": "183831"
}

'''response = requests.post(url =f'{URL}/trainers/reg', headers= HEADER, json = body_registration )
print(response.text)'''

response_create=requests.post(url = f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)

'''pokemon_id = response_create.json()['id']
print(pokemon_id)'''

message = response_create.json()['message']
print(message)

response_new_name=requests.patch(url = f'{URL}/pokemons', headers= HEADER, json= body_new_name)
print(response_new_name.text)
message = response_new_name.json()['message']
print(message)

response_pokeball=requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_pokeball)
print(response_pokeball.text)
message = response_pokeball.json()['message']
print(message)