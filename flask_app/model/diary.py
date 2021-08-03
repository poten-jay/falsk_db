import csv
import psycopg2

host = 'arjuna.db.elephantsql.com'
user = 'qgjwncfp'
password = 'DjfynfwLe5OuKO0aS1XsEiJMA2oT17e_'
database = 'qgjwncfp'

# host = 'rosie.db.elephantsql.com'
# user = 'blhrawxv'
# password = 'zwcQOCt7eYPxqw6X8CmAGxy_PQfP8WW-'
# database = 'blhrawxv'


connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# https://api.elephantsql.com/console/003c79b5-5719-4a95-b00f-27a38da9a3e1/details


# 커서
cur = connection.cursor()

# 열 조건 (테이블 만들기)
cur.execute("""CREATE TABLE ck_diary (
                id  INTEGER PRIMARY KEY,
                chicken VARCHAR(128) NOT NULL                
                );
            """)


# Commit 
connection.commit()

