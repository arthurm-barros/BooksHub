from flask import Flask
from core.database import db
from core import blueprints
from seed import popular
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
blueprints.init_app(app)
with app.app_context():
    popular()

if __name__ == '__main__':
    app.run(debug=True)