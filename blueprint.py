from flask import Blueprint
from src.controller.indexController import *


bp = Blueprint("blueprint", __name__)

bp.route("/", methods=["GET"])(index)
