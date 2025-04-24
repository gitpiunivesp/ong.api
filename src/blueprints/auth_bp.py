from flask import Blueprint, Response, request

from src.models.usuario import Usuario
from src.helpers import vectorize

from playhouse.shortcuts import dict_to_model

import json

auth_bp = Blueprint('auth', __name__, url_prefix='/')

@auth_bp.post("/login")
def login():
    try:
        Usuario.get(Usuario.email == request.json.get("email"), Usuario.senha == request.json.get("password"))

        return Response(json.dumps({"mensagem": "Logado com sucesso"}), status=200)
    except:
        return Response(json.dumps({"mensagem": "Não autorizado"}), status=401)

@auth_bp.post("/register")
def register():
    usuario = dict_to_model(Usuario, request.json, ignore_unknown=True)
    usuario.search_vector = vectorize(request.json)
    usuario.save()

    return Response(json.dumps({"mensagem": "Registrado com sucesso"}), status=200)