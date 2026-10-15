from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sqla
from sqlalchemy.orm import relationship, mapped_column, Mapped, DeclarativeBase
from typing import List
class Base(DeclarativeBase):
    pass

db = SQLAlchemy()

livro_categoria = db.Table(
    'livro_categoria',
    db.metadata,
    sqla.Column('livro_id', sqla.ForeignKey('livros.id'), primary_key=True),
    sqla.Column('categoria_id', sqla.ForeignKey('categorias.id'), primary_key=True)
)
class Autor(db.Model):
    __tablename__ = 'autores'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(sqla.String(64), unique=True)
    livros: Mapped[List['Livro']] = relationship(back_populates='autor')

class Livro(db.Model):
    __tablename__ = 'livros'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(sqla.String(48), unique=True)
    ano: Mapped[int] = mapped_column()
    sinopse: Mapped[str] = mapped_column(sqla.Text())
    avaliacao: Mapped[float] = mapped_column()

    autor_id: Mapped[int] = mapped_column(sqla.ForeignKey('autores.id'))
    autor: Mapped['Autor'] = relationship(back_populates='livros')

    categorias: Mapped[List['Categoria']] = relationship(secondary=livro_categoria, back_populates='livros')

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(sqla.String(24), unique=True)

    livros: Mapped[List['Livro']] = relationship(secondary=livro_categoria, back_populates='categorias')


