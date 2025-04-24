from flask import Blueprint, Response, request

from src.models.animal import Animal
from src.helpers import jsonify, vectorize

from playhouse.shortcuts import dict_to_model, update_model_from_dict

animal_bp = Blueprint('animal', __name__, url_prefix='/animais')

@animal_bp.route("", methods=["GET"])
def index():
    text_search = request.args.get("q")

    animals = Animal.select().where(Animal.search_vector.match(text_search)) if text_search else Animal.select()

    return jsonify(animals, Animal)

@animal_bp.route("<id>", methods=["GET"])
def show(id):
    return jsonify(Animal.get_by_id(id), Animal)

@animal_bp.route("", methods=["POST"])
def create():
    animal = dict_to_model(Animal, request.json, ignore_unknown=True)
    animal.search_vector = vectorize(request.json)
    animal.save()

    return Response(jsonify(animal, Animal), status=201)

@animal_bp.route("<id>", methods=["PUT"])
def update(id):
    animal = Animal.get_by_id(id)

    animal_updated = update_model_from_dict(animal, request.json)
    animal_updated.search_vector = vectorize(request.json)
    animal_updated.save()

    return Response(jsonify(animal_updated, Animal), status=200)

@animal_bp.route("<id>", methods=["DELETE"])
def delete(id):
    Animal.delete_by_id(id)

    return Response(status=204)