from flask import render_template, url_for, request, redirect
from ...database import db, Livro, Autor, Categoria

from . import autor_bp

@autor_bp.route('/autores')
def listar():
    autores = db.session.scalars(db.select(Autor)).all()
    return render_template('aut_listar.html', autores=autores)

@autor_bp.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    autor = db.get_or_404(Autor, id)
    db.session.delete(autor)
    db.session.commit()
    return redirect(url_for('autores.listar'))

@autor_bp.route('/criar', methods=["POST",'GET'])
def criar():
    if request.method == 'POST':

        nome = request.form.get('nome')

        if nome:

            novo = Autor(nome=nome)
            db.session.add(novo)
            db.session.commit()

            return redirect(url_for('autores.listar'))
    return render_template('aut_criar.html')