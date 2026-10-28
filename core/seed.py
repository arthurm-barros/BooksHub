from .database import db, Autor, Livro, Categoria

def popular():
    db.create_all()

    if Livro.query.first():
        return

    autor1 = Autor(nome="Robertinho")
    autor2 = Autor(nome="Dorival")

    cat_fantasias = Categoria(titulo="Fantasia")
    cat_ficcao = Categoria(titulo="Ficção Científica")
    cat_classicos = Categoria(titulo="Clássicos")

    livro1 = Livro( titulo="O Senhor", ano=2022, sinopse="Uma jornada épica de um senhor.", avaliacao=4.9, autor=autor1, categorias=[cat_fantasias, cat_classicos])

    livro2 = Livro( titulo="1111", ano=2222, sinopse="Uma distopia sobre alguma coisa.", avaliacao=4.8, autor=autor2, categorias=[cat_ficcao, cat_classicos])

    # 4. Salva no banco de dados
    db.session.add_all([autor1, autor2, cat_fantasias, cat_ficcao, cat_classicos, livro1, livro2])
    db.session.commit()
    print("Banco de dados populado")