from flask import Blueprint, Response

from src.models.animal import Animal
from src.models.tutor import Tutor
from src.models.agendamento import Agendamento

from src.helpers import jsonify

import json

relatorio_bp = Blueprint('relatorio', __name__, url_prefix='/relatorios')

@relatorio_bp.get("/animais_da_ong")
def animais_da_ong():
    animais = Animal.select().where(Animal.tutor.is_null())

    return Response(jsonify(animais, Animal))

@relatorio_bp.get("/possiveis_tutores")
def possiveis_tutores():
    return Response(jsonify(Tutor.select(), Tutor))

@relatorio_bp.get("/animais_adotados")
def animais_adotados():
    animais = Animal.select().where(~Animal.tutor.is_null())
    return Response(jsonify(animais, Animal))

@relatorio_bp.get("/animais_vacinados")
def animais_vacinados():
    animais = Animal.select(Animal.id, Animal.especie, Agendamento.data).join(Agendamento, on=(Agendamento.animal == Animal.id)).where(Agendamento.procedimento == "VACINACAO").dicts()

    return Response(json.dumps(list(animais), default=str))

@relatorio_bp.get("/animais_castrados")
def animais_castrados():
    animais = Animal.select(Animal.id, Animal.especie, Agendamento.data).join(Agendamento, on=(Agendamento.animal == Animal.id)).where(Agendamento.procedimento == "CASTRACAO").dicts()
    return Response(json.dumps(list(animais), default=str))