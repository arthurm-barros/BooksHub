from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sqla
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Livro(db.Model):
    __tablename__ = 'livros'

    id = sqla.Column(type_=sqla.Integer(), primary_key=True, autoincrement=True)
    titulo = sqla.Column(type_=sqla.String(48), unique=True)
    ano = sqla.Column(type_=sqla.Integer())
    sinopse = sqla.Column(type_=sqla.Text())
    avaliacao = sqla.Column(type_=sqla.Float())
    autor = relationship('livros', back_populates='livros')
    categorias = relationship(
        'categorias',
        secondary='livro_categoria',
        back_populates='livros'
    )


class Autor(db.Model):
    __tablename__ = 'autores'

    id = sqla.Column(type_=sqla.Integer(), primary_key=True, autoincrement=True)
    nome = sqla.Column(type_=sqla.String(64), unique=True)


livro_categoria = db.Table(
    'livro_categoria',
    sqla.Column('livro_id', sqla.ForeignKey('livros.id')),
    sqla.Column('categoria_id', sqla.ForeignKey('categorias.id'))
)


class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = sqla.Column(type_=sqla.Integer(), primary_key=True, autoincrement=True)
    titulo = sqla.Column(type_=sqla.String(24), unique=True)