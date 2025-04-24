from playhouse.postgres_ext import *
from peewee import *

from src.database import db

from src.models.tutor import Tutor
from src.models.animal import Animal
from src.models.colaborador import Colaborador

class Agendamento(Model):
    data = DateField()
    procedimento = CharField()
    tutor = ForeignKeyField(Tutor, null=True)
    animal = ForeignKeyField(Animal, null=True)
    colaborador = ForeignKeyField(Colaborador, null=True)
    search_vector = TSVectorField()

    class Meta:
        database = db
        table_name = "agendamentos"
