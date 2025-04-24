from playhouse.postgres_ext import *
from peewee import *

from src.database import db

class Usuario(Model):
    nome = CharField()
    usuario = CharField()
    senha = CharField()
    email = CharField()
    telefone = CharField()
    search_vector = TSVectorField()

    class Meta:
        database = db
        table_name = "usuarios"
