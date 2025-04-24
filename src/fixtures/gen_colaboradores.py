from faker import Faker

import json, requests

fake = Faker("pt_BR")

for i in range(500):
    requests.post(url="http://localhost:5000/colaboradores", data=json.dumps({
        "nome": fake.name(),
        "cpf": fake.cpf(),
        "endereco": fake.street_address(),
        "telefone": fake.phone_number(),
        "email": fake.email(),
        "anotacoes": fake.sentence(),
    }), headers={"Content-Type": "application/json"})

