import mysql.connector
username = input('username:')
password = input('password:')
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)

cursor = conn.cursor()
# Create a database 'accounts' where accounts would be stored with id, username, password
cursor.execute('CREATE DATABASE IF NOT EXISTS accounts')
conn.database = 'accounts'
# Creates a table with colums ID, USERNAME, PASSWORD
cursor.execute('CREATE TABLE IF NOT EXISTS account (id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(60) UNIQUE NOT NULL, password VARCHAR(60) NOT NULL)')

try:
    cursor.execute(f'INSERT INTO account(username, password) VALUES (%s, %s)', (username, password))
    conn.commit()
except mysql.connector.errors.IntegrityError as a:
    print(f'Error username {username} already exists')

cursor.execute('SELECT * FROM account')
result = cursor.fetchall()
for table in result:
    print(table)