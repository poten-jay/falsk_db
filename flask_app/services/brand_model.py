from sqlalchemy.orm import backref
from flask_app import db

class Brand(db.Model):
    __tablename__ = 'brand'

    id = db.Column(db.Integer(),primary_key=True)
    brand = db.Column(db.String(64), nullable=False )
    s_count = db.Column(db.Integer())
    s_start  = db.Column(db.String(64), nullable=False)
    s_year  = db.Column(db.Integer())


    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

    tweets = db.relationship('Menu', backref='user', cascade = 'all, delete')

    def __repr__(self):
        return f"Brand {self.id}"



# FLASK_APP=twit_app flask run


