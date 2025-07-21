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

cursor.execute('CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY, name VARCHAR(64))')
cursor.execute('''
INSERT INTO person (id,name) VALUES (1, 'greqg'); ''')
conn.commit()
cursor.execute('SELECT * FROM person')
result = cursor.fetchall()
for table in result:
    print(table)