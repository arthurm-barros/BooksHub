from flask import Blueprint
import os

template = os.path.join(os.path.dirname(__file__), 'templates')
cat_bp = Blueprint("categorias", __name__, template_folder=template)

from . import routes