from flask import render_template, url_for, request, redirect
from core.database import db, Livro, Autor, Categoria

from . import livro_bp

@livro_bp.route('/livros')
def listar():
    livros = db.session.scalars(db.select(Livro)).all()
    return render_template('li_listar.html', livros=livros)

@livro_bp.route('/editar/<int:id>', methods=['POST','GET'])
def editar(id):
    livro = db.get_or_404(Livro, id)

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        ano = int(request.form.get('ano'))
        avaliacao = float(request.form.get('avaliacao'))
        sinopse = request.form.get('sinopse')
        autor_id = int(request.form.get('autor_id'))
        if titulo and ano and avaliacao and sinopse and autor_id:
            livro.titulo = titulo
            livro.ano = ano
            livro.avaliacao = avaliacao
            livro.sinopse = sinopse
            livro.autor_id = autor_id

            categorias = request.form.getlist('categorias')
            livro.categorias = db.session.scalars(db.select(Categoria).where(Categoria.id.in_(categorias))).all()
            db.session.commit()
            return redirect(url_for('livros.listar'))

    autores = db.session.scalars(db.select(Autor)).all()
    categorias = db.session.scalars(db.select(Categoria)).all()
    return render_template('li_editar.html', livro=livro, categorias=categorias, autores=autores)

@livro_bp.route('/deletar/<int:id>', methods=['POST'])
def deletar(id):
    livro = db.get_or_404(Livro, id)
    db.session.delete(livro)
    db.session.commit()
    return redirect(url_for('livros.listar'))

@livro_bp.route('/criar', methods=["POST",'GET'])
def criar():
    if request.method == 'POST':

        titulo = request.form.get('titulo')
        ano = int(request.form.get('ano'))
        avaliacao = float(request.form.get('avaliacao'))
        sinopse = request.form.get('sinopse')
        autor_id = int(request.form.get('autor_id'))

        if titulo and ano and avaliacao and sinopse and autor_id:

            novo = Livro(titulo=titulo, ano=ano, avaliacao=avaliacao, sinopse=sinopse, autor_id=autor_id)
            categorias_id = request.form.getlist('categorias')

            if categorias_id:

                cate_select = db.session.scalars(db.select(Categoria).where(Categoria.id.in_(categorias_id))).all()
                novo.categorias = cate_select
            db.session.add(novo)
            db.session.commit()
            return redirect(url_for('livros.listar'))

    autores = db.session.scalars(db.select(Autor)).all()
    categorias = db.session.scalars(db.select(Categoria)).all()
    return render_template('li_criar.html', autores=autores, categorias=categorias);