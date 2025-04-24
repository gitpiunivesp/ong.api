from flask import Blueprint, Response, request

from src.models.agendamento import Agendamento
from src.helpers import jsonify, vectorize

from playhouse.shortcuts import dict_to_model, update_model_from_dict

agendamento_bp = Blueprint('agendamento', __name__, url_prefix='/agendamentos')

@agendamento_bp.route("", methods=["GET"])
def index():
    text_search = request.args.get("q")

    agendamentos = Agendamento.select().where(Agendamento.search_vector.match(text_search)) if text_search else Agendamento.select()

    return jsonify(agendamentos, Agendamento)

@agendamento_bp.route("<id>", methods=["GET"])
def show(id):
    return jsonify(Agendamento.get_by_id(id), Agendamento)

@agendamento_bp.route("", methods=["POST"])
def create():
    agendamento = dict_to_model(Agendamento, request.json, ignore_unknown=True)
    agendamento.search_vector = vectorize(request.json)
    agendamento.save()

    return Response(jsonify(agendamento, Agendamento), status=201)

@agendamento_bp.route("<id>", methods=["PUT"])
def update(id):
    agendamento = Agendamento.get_by_id(id)

    agendamento_updated = update_model_from_dict(agendamento, request.json)
    agendamento_updated.search_vector = vectorize(request.json)
    agendamento_updated.save()

    return Response(jsonify(agendamento_updated, Agendamento), status=200)

@agendamento_bp.route("<id>", methods=["DELETE"])
def delete(id):
    Agendamento.delete_by_id(id)

    return Response(status=204)