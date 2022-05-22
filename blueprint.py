from flask import Blueprint
from src.controller.indexController import *


bp = Blueprint("blueprint", __name__)

bp.route("/", methods=["GET"])(listar)
bp.route("/cadastrar", methods=["POST"])(cadastrar)
bp.route("/alterar/<id>", methods=["GET"])(alterar)
bp.route("/salvar", methods=["POST"])(salvar)
bp.route("/deletar", methods=["GET"])(deletar)
