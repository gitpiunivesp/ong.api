from flask import Blueprint, Response, request

from src.models.usuario import Usuario
from src.helpers import jsonify, vectorize

from playhouse.shortcuts import dict_to_model, update_model_from_dict

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_bp.route("", methods=["GET"])
def index():
    text_search = request.args.get("q")

    usuarios = Usuario.select().where(Usuario.search_vector.match(text_search)) if text_search else Usuario.select()

    return jsonify(usuarios, Usuario)

@usuario_bp.route("<id>", methods=["GET"])
def show(id):
    return jsonify(Usuario.get_by_id(id), Usuario)

@usuario_bp.route("", methods=["POST"])
def create():
    usuario = dict_to_model(Usuario, request.json, ignore_unknown=True)
    usuario.search_vector = vectorize(request.json)
    usuario.save()

    return Response(jsonify(usuario, Usuario), status=201)

@usuario_bp.route("<id>", methods=["PUT"])
def update(id):
    usuario = Usuario.get_by_id(id)

    usuario_updated = update_model_from_dict(usuario, request.json)
    usuario_updated.search_vector = vectorize(request.json)
    usuario_updated.save()

    return Response(jsonify(usuario_updated, Usuario), status=200)

@usuario_bp.route("<id>", methods=["DELETE"])
def delete(id):
    Usuario.delete_by_id(id)

    return Response(status=204)