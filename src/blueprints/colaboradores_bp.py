from flask import Blueprint, Response, request

from src.models.colaborador import Colaborador
from src.helpers import jsonify, vectorize

from playhouse.shortcuts import dict_to_model, update_model_from_dict

colaborador_bp = Blueprint('colaborador', __name__, url_prefix='/colaboradores')

@colaborador_bp.route("", methods=["GET"])
def index():
    text_search = request.args.get("q")

    colaboradors = Colaborador.select().where(Colaborador.search_vector.match(text_search)) if text_search else Colaborador.select()

    return jsonify(colaboradors, Colaborador)

@colaborador_bp.route("<id>", methods=["GET"])
def show(id):
    return jsonify(Colaborador.get_by_id(id), Colaborador)

@colaborador_bp.route("", methods=["POST"])
def create():
    colaborador = dict_to_model(Colaborador, request.json, ignore_unknown=True)
    colaborador.search_vector = vectorize(request.json)
    colaborador.save()

    return Response(jsonify(colaborador, Colaborador), status=201)

@colaborador_bp.route("<id>", methods=["PUT"])
def update(id):
    colaborador = Colaborador.get_by_id(id)

    colaborador_updated = update_model_from_dict(colaborador, request.json)
    colaborador_updated.search_vector = vectorize(request.json)
    colaborador_updated.save()

    return Response(jsonify(colaborador_updated, Colaborador), status=200)

@colaborador_bp.route("<id>", methods=["DELETE"])
def delete(id):
    Colaborador.delete_by_id(id)

    return Response(status=204)