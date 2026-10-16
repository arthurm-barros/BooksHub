from .livros import livro_bp
# from .autores import autor_bp
# from .categorias import cate_bp
def init_app(app):
    app.register_blueprint(livro_bp)
    # app.register_blueprint(autor_bp)
    # app.register_blueprint(cate_bp)