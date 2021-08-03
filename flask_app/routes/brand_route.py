# import csv
# from re import L
# import psycopg2
from flask import Blueprint, request, render_template
from flask_app.model.data_base import cur, cur1
from flask_app import db
from random import randint

bp = Blueprint('user', __name__)


@bp.route('/user', methods=['GET'])
def brand_list():

    cur.execute('SELECT * FROM ck_brand;')
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

@bp.route('/compare', methods=['GET'])
def random_ck():


    cur1.execute('SELECT * FROM ck_menu;')
    result1 = cur1.fetchall()

    ran_ck = []
    for k in range(0,len(result1)-1):
        ran_ck.append([result1[k][2], result1[k][3]])

    return ran_ck[randint(0,len(result1)-1)]


# cur1.execute('SELECT * FROM ck_menu;')
# result1 = cur1.fetchall()
# ran_ck = []
# for k in range(0,len(result1)-1):
#     ran_ck.append([result1[k][2], result1[k][3]])

# ran_ck[randint(0,len(result1)-1)]

