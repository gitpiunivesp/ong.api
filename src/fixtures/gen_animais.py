from faker import Faker

import json, requests, random

fake = Faker("pt_BR")

for i in range(500):
    first_name = fake.first_name()

    requests.post(url="http://localhost:5000/animais", data=json.dumps({
        "nome": first_name,
        "data_entrada": fake.date(),
        "data_adocao": fake.date(),
        "apelido": first_name.lower(),
        "anotacoes": fake.sentence(),
        "especie": random.choice(["CAO", "GATO"]),
        "tutor_id": fake.pyint(min_value=1, max_value=500),
    }), headers={"Content-Type": "application/json"})

for i in range(500):
    first_name = fake.first_name()

    requests.post(url="http://localhost:5000/animais", data=json.dumps({
        "nome": first_name,
        "data_entrada": fake.date(),
        "data_adocao": fake.date(),
        "apelido": first_name.lower(),
        "anotacoes": fake.sentence(),
        "especie": random.choice(["CAO", "GATO"]),
    }), headers={"Content-Type": "application/json"})