import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)

print(conn)