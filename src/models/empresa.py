from playhouse.postgres_ext import *
from peewee import *

from src.database import db

class Empresa(Model):
    cnpj = CharField()
    email = CharField()
    endereco = CharField()
    nome_fantasia = CharField()
    razao_social = CharField()
    telefone = CharField()
    search_vector = TSVectorField()

    class Meta:
        database = db
        table_name = "empresas"
