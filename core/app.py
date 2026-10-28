import os
from flask import Flask, render_template
from .database import db
from . import blueprints
from .seed import popular
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')
app.config['CONTENT_MAX_LENGTH'] = 5 * 1024 * 1024

db.init_app(app)
blueprints.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        popular()
    app.run(debug=True)