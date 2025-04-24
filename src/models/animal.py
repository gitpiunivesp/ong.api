from playhouse.postgres_ext import *
from peewee import *

from src.database import db

from src.models.tutor import Tutor

class Animal(Model):
    nome = CharField(null=True)
    data_entrada = DateField(null=True)
    data_adocao = DateField(null=True)
    apelido = CharField(null=True)
    anotacoes = TextField(null=True)
    especie = CharField(null=True)
    raca = CharField(null=True)
    porte = CharField(null=True)
    cor = CharField(null=True)
    peso = CharField(null=True)
    tutor = ForeignKeyField(Tutor, null=True)
    search_vector = TSVectorField()

    class Meta:
        database = db
        table_name = "animais"
