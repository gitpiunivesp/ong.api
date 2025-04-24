from flask import Blueprint, Response, request

from src.models.empresa import Empresa
from src.helpers import jsonify, vectorize

from playhouse.shortcuts import dict_to_model, update_model_from_dict

empresa_bp = Blueprint('empresa', __name__, url_prefix='/empresas')

@empresa_bp.route("", methods=["GET"])
def index():
    text_search = request.args.get("q")

    empresas = Empresa.select().where(Empresa.search_vector.match(text_search)) if text_search else Empresa.select()

    return jsonify(empresas, Empresa)

@empresa_bp.route("<id>", methods=["GET"])
def show(id):
    return jsonify(Empresa.get_by_id(id), Empresa)

@empresa_bp.route("", methods=["POST"])
def create():
    empresa = dict_to_model(Empresa, request.json, ignore_unknown=True)
    empresa.search_vector = vectorize(request.json)
    empresa.save()

    return Response(jsonify(empresa, Empresa), status=201)

@empresa_bp.route("<id>", methods=["PUT"])
def update(id):
    empresa = Empresa.get_by_id(id)

    empresa_updated = update_model_from_dict(empresa, request.json)
    empresa_updated.search_vector = vectorize(request.json)
    empresa_updated.save()

    return Response(jsonify(empresa_updated, Empresa), status=200)

@empresa_bp.route("<id>", methods=["DELETE"])
def delete(id):
    Empresa.delete_by_id(id)

    return Response(status=204)