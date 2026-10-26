from flask import Flask, render_template
from .database import db
from . import blueprints
from .seed import popular
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
blueprints.init_app(app)
with app.app_context():
    popular()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)