from faker import Faker

import json, requests

fake = Faker("pt_BR")

for i in range(500):
    company_name = fake.company()

    requests.post(url="http://localhost:5000/empresas", data=json.dumps({
        "cnpj": fake.cnpj(),
        "email": fake.company_email(),
        "endereco": fake.street_address(),
        "nome_fantasia": company_name,
        "razao_social": f"{company_name} {fake.company_suffix()}",
        "telefone": fake.phone_number()
    }), headers={"Content-Type": "application/json"})

