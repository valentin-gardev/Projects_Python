import mysql.connector
login = int(input('1. Login, 2. Register::'))
username = input('username:')
password = input('password:')
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)


def register_account():
    try:
        cursor.execute(f'INSERT INTO account(username, password) VALUES (%s, %s)', (username, password))
        conn.commit()
    except mysql.connector.errors.IntegrityError as a:
        print(f'Error username {username} already exists')


def login_account():
    cursor.execute('SELECT password FROM account WHERE username = %s', (username,))
    result_of_login = cursor.fetchone()

    if result_of_login:
        stored_password = result_of_login[0]
        if stored_password == password:
            print('Correct password')
        else:
            print('incorrect password')
    else:
        print('Username does not exist')


def delete_account():
    cursor.execute('DELETE FROM account WHERE username = %s', (username,))
    
    
cursor = conn.cursor()
# Create a database 'accounts' where accounts would be stored with id, username, password
cursor.execute('CREATE DATABASE IF NOT EXISTS accounts')
conn.database = 'accounts'
# Creates a table with colums ID, USERNAME, PASSWORD
cursor.execute('CREATE TABLE IF NOT EXISTS account (id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(60) UNIQUE NOT NULL, password VARCHAR(60) NOT NULL)')

if login == 1:
    login_account()
elif login == 2:
    register_account()



cursor.execute('SELECT * FROM account')
result = cursor.fetchall()
for table in result:
    print(table)