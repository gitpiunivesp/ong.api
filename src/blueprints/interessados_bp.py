from flask import Blueprint, Response, request

from src.models.interessado import Interessado
from src.helpers import jsonify, vectorize

from playhouse.shortcuts import dict_to_model, update_model_from_dict

interessado_bp = Blueprint('interessado', __name__, url_prefix='/interessados')

@interessado_bp.route("", methods=["GET"])
def index():
    text_search = request.args.get("q")

    interessados = Interessado.select().where(Interessado.search_vector.match(text_search)) if text_search else Interessado.select()

    return jsonify(interessados, Interessado)

@interessado_bp.route("<id>", methods=["GET"])
def show(id):
    return jsonify(Interessado.get_by_id(id), Interessado)

@interessado_bp.route("", methods=["POST"])
def create():
    interessado = dict_to_model(Interessado, request.json, ignore_unknown=True)
    interessado.search_vector = vectorize(request.json)
    interessado.save()

    return Response(jsonify(interessado, Interessado), status=201)

@interessado_bp.route("<id>", methods=["PUT"])
def update(id):
    interessado = Interessado.get_by_id(id)

    interessado_updated = update_model_from_dict(interessado, request.json)
    interessado_updated.search_vector = vectorize(request.json)
    interessado_updated.save()

    return Response(jsonify(interessado_updated, Interessado), status=200)

@interessado_bp.route("<id>", methods=["DELETE"])
def delete(id):
    Interessado.delete_by_id(id)

    return Response(status=204)