from faker import Faker

import json, requests

fake = Faker("pt_BR")

for i in range(500):
    requests.post(url="http://localhost:5000/usuarios", data=json.dumps({
        "nome": fake.name(),
        "usuario": fake.user_name(),
        "senha": fake.password(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
    }), headers={"Content-Type": "application/json"})

