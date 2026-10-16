from flask import render_template, url_for, request, redirect
from core.database import db, Livro, Autor, Categoria

from . import cat_bp

@cat_bp.route('/')
def listar():
    categorias = db.session.scalars(db.select(Categoria)).all()
    return render_template('cat_listar.html', categorias=categorias)

