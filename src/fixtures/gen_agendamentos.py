from faker import Faker

import json, requests, random

fake = Faker("pt_BR")

for i in range(500):
    first_name = fake.first_name()

    requests.post(url="http://localhost:5000/agendamentos", data=json.dumps({
        "data": fake.date(),
        "procedimento": random.choice(["CASTRACAO", "VACINACAO"]),
        "animal_id": fake.pyint(min_value=1, max_value=500),
        "colaborador_id": fake.pyint(min_value=1, max_value=500),
        "tutor_id": fake.pyint(min_value=1, max_value=500)
    }), headers={"Content-Type": "application/json"})