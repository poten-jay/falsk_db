# main_route

from flask import Blueprint, render_template, request
from flask_app import db

# from py_flask_app.models import db, User  # model 것들을 여기서 작업하고 싶을때,,


bp = Blueprint('main', __name__)

@bp.route('/')                          # app 을 bp로 바꿔줌
def index():
    return render_template('index.html')

@bp.route('/user')                    # main_route로 옮겨 줌
def create():
#    User.query
    return render_template('user.html')


@bp.route('/compare')
def update():
    return render_template('compare_user.html')