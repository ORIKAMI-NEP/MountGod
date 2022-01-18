import pymysql.cursors
import json

with open("json/password.json", "r", encoding="utf-8") as Password:
    connection = pymysql.connect(host="localhost",
        user="root",
        password=json.load(Password)["password"],
        db="MountGod",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "INSERT INTO LearnedData (message, password) VALUES (%s, %s)"
    cursor.execute(sql, ('test1', 'test2'))
connection.commit()

try:
    with connection.cursor() as cursor:
        cursor=connection.cursor(pymysql.cursors.DictCursor)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()