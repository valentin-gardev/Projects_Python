import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='accounts'
)

cursor = conn.cursor()
# Create a database 'accounts' where accounts would be stored with id, username, password
cursor.execute('CREATE DATABASE IF NOT EXISTS accounts')

cursor.execute('CREATE TABLE IF NOT EXISTS id INT PRIMARY KEY AUTOINCREMENT,'
               'username TEXT UNIQUE NOT NULL,'
               'password TEXT NOT NULL')