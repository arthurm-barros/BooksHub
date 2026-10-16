from flask import render_template, url_for, request
from core.database import db, Livro

from . import livro_bp

@livro_bp.route('/')
def listar():
    livros = db.session.scalars(db.select(Livro)).all()
    return render_template('listar.html', livros=livros)