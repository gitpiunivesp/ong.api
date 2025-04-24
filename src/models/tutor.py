from playhouse.postgres_ext import *
from peewee import *

from src.database import db

class Tutor(Model):
    nome = CharField()
    cpf = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()
    anotacoes = TextField()
    search_vector = TSVectorField()

    class Meta:
        database = db
        table_name = "tutores"
