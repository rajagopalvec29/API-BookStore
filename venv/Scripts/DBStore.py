import requests
import os
import cx_Oracle
os.environ['PATH'] = "E:\\instantclient_21_9"

con = cx_Oracle.connect(user = "SYSTEM",password = "sys123",dsn = "DESKTOP-TT53EVU/XE")
cur = con.cursor()


query = "select * from student_marksheet"
cur.execute(query)
rows = cur.fetchall()
for row in rows:
    print(row)

