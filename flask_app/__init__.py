# __init__.py     (초기 시작)

from flask import Flask
from flask_app.models import db, migrate  # models 파일로 접근해서 db, mg 접근

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, migrate

# db = SQLAlchemy()
# migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # @app.route('/')
    # def index():
    #     return 'Welcome to Index Page'

    # @app.route('/create')
    # def create():
    #     return 'Welcome to Create Page'
    
    # @app.route('/update')
    # def update():
    #     return 'Welcome to Update Page'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///test.db'

    db.init_app(app)    
    migrate.init_app(app, db) 

    from flask_app.routes import main_route
    app.register_blueprint(main_route.bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run

# FLASK_APP=flask_app flask run

# FLASK_APP=flask_app flask db init   <- migration 폴더 생김

# FLASK_APP=flask_app flask db migrate   <- db 생성

# FLASK_APP=flask_app flask db upgrade   <- 업그레이드

# 일련의 작헙 후 
# FLASK_APP=flask_app flask db migrate   <- 버전이 새로 생김

# FLASK_APP=flask_app flask db upgrade   <- db에 적용
# db 에 버전이 업뎃 되고 user 테이블이 만들어짐