# models.py

# from flask_app import db

from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String(32))

    def __repr__(self):
        return 'User %i, name is %s' % (self.id, self.name)