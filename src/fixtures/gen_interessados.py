from faker import Faker

import json, requests

fake = Faker("pt_BR")

for i in range(500):
    company_name = fake.company()

    requests.post(url="http://localhost:5000/interessados", data=json.dumps({
        "nome": fake.name(),
        "endereco": fake.street_address(),
        "telefone": fake.phone_number(),
        "email": fake.email(),
        "rede_social": fake.user_name(),
        "anotacoes": fake.sentence()
    }), headers={"Content-Type": "application/json"})