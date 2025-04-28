from playhouse.postgres_ext import *
from peewee import *

from src.database import db

class Interessado(Model):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()
    rede_social = CharField()
    # anotacoes = TextField()
    anotacoes = TextField(null=True)
    search_vector = TSVectorField()

    class Meta:
        database = db
        table_name = "interessados"
