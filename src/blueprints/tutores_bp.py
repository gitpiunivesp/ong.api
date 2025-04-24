from flask import Blueprint, Response, request

from src.models.tutor import Tutor
from src.helpers import jsonify, vectorize

from playhouse.shortcuts import dict_to_model, update_model_from_dict

tutor_bp = Blueprint('tutor', __name__, url_prefix='/tutores')

@tutor_bp.route("", methods=["GET"])
def index():
    text_search = request.args.get("q")

    tutores = Tutor.select().where(Tutor.search_vector.match(text_search)) if text_search else Tutor.select()

    return jsonify(tutores, Tutor)

@tutor_bp.route("<id>", methods=["GET"])
def show(id):
    return jsonify(Tutor.get_by_id(id), Tutor)

@tutor_bp.route("", methods=["POST"])
def create():
    tutor = dict_to_model(Tutor, request.json, ignore_unknown=True)
    tutor.search_vector = vectorize(request.json)
    tutor.save()

    return Response(jsonify(tutor, Tutor), status=201)

@tutor_bp.route("<id>", methods=["PUT"])
def update(id):
    tutor = Tutor.get_by_id(id)

    tutor_updated = update_model_from_dict(tutor, request.json)
    tutor_updated.search_vector = vectorize(request.json)
    tutor_updated.save()

    return Response(jsonify(tutor_updated, Tutor), status=200)

@tutor_bp.route("<id>", methods=["DELETE"])
def delete(id):
    Tutor.delete_by_id(id)

    return Response(status=204)