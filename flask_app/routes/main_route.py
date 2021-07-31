# main_route

from flask import Blueprint

# from py_flask_app.models import db, User  # model 것들을 여기서 작업하고 싶을때,,


bp = Blueprint('main', __name__)

@bp.route('/')                          # app 을 bp로 바꿔줌
def index():
    return 'Welcome to Index Page'

@bp.route('/create')                    # main_route로 옮겨 줌
def create():
#    User.query
    return 'Welcome to Create Page'

@bp.route('/update')
def update():
    return 'Welcome to Update Page'