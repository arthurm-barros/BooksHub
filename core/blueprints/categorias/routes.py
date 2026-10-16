from flask import render_template, url_for, request, redirect
from core.database import db, Livro, Autor, Categoria

from . import cat_bp

@cat_bp.route('/')
def listar():
    categorias = db.session.scalars(db.select(Categoria)).all()
    return render_template('cat_listar.html', categorias=categorias)

@cat_bp.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    categoria = db.get_or_404(Categoria, id)
    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('categorias.listar'))

@cat_bp.route('/criar', methods=["POST",'GET'])
def criar():
    if request.method == 'POST':

        titulo = request.form.get('titulo')

        if titulo:

            novo = Categoria(titulo=titulo)
            db.session.add(novo)
            db.session.commit()

            return redirect(url_for('categorias.listar'))
    return render_template('cat_criar.html')
