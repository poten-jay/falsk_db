# import csv
# from re import L
# import psycopg2
from flask import Blueprint, request, render_template
from flask_app.model.data_base import cur
from flask_app import db

bp = Blueprint('user', __name__)


@bp.route('/user', methods=['GET'])
def brand_list():

    #cur.execute('SELECT * FROM ck_brand;')
    result = cur.fetchall()
    # (0, 'BBQ치킨', 1659, '경기', 1995)

    brand_list_list = []
    for i in range(0,len(result)-1):
        brand_list_list.append([result[i][0],result[i][1].strip()])

    b_list = []
    for i in range(0,len(result)-1):
        b_list.append(
            {'id' : brand_list_list[i][0], 'brand' : brand_list_list[i][1]}
            )

    return render_template('user.html', b_list=b_list), 200

#brand_dict[0].id


@bp.route('/user', methods=['POST'])
def add_user():

    return None



#    brand_list = request.form.get('username')

#   username = request.form.get('ck_brand')

