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

cursor.execute('CREATE TABLE IF NOT EXISTS account (id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(60) UNIQUE NOT NULL, password VARCHAR(60) NOT NULL)')
# cursor.execute()
conn.commit()
cursor.execute('SELECT * FROM account')
result = cursor.fetchall()
for table in result:
    print(table)