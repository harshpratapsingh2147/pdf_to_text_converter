import pymysql
import re

HOST = '54.188.17.63'
NAME = 'visionias_in'
USER = 'fixxer'
PASS = '7$zPxE!2wH6q'
PORT = 3306

def connect_to_db():
    try:
        print("trying to connect to database....")
        print(HOST)
        conn = pymysql.connect(host=HOST, user=USER, passwd=PASS, db=NAME, port=3306, connect_timeout=5)
        print(f"connect to db....{conn}")
    except pymysql.MySQLError as err:
        print(err)

connect_to_db()