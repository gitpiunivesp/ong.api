from playhouse.postgres_ext import *
from peewee import *

from src.database import db

class Colaborador(Model):
    nome = CharField()
    cpf = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()
    # anotacoes = TextField()
    anotacoes = TextField(null=True)
    search_vector = TSVectorField()

    class Meta:
        database = db
        table_name = "colaboradores"
