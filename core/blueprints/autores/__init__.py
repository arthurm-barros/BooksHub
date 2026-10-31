from flask import Blueprint
import os

template = os.path.join(os.path.dirname(__file__), 'templates')
autor_bp = Blueprint("autores", __name__, template_folder=template)

from . import routes