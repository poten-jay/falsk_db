from flask_sqlalchemy import SQLAlchemy
from flask_app import db


class Menu(db.Model):
    __tablename__ = 'menu'

    no = db.Column(db.Integer(), primary_key=True)
    brand_id = db.Column(db.Integer())
    brand = db.Column(db.String(64), db.ForeignKey('brand.id'))
    menu  = db.Column(db.String(64))


    def __repr__(self):
        return f"Menu {self.id}"




