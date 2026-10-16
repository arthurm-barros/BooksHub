from .livros import livro_bp
# from .autores import autor_bp
from .categorias import cat_bp
def init_app(app):
    app.register_blueprint(livro_bp)
    # app.register_blueprint(autor_bp)
    app.register_blueprint(cat_bp, url_prefix='/categorias')