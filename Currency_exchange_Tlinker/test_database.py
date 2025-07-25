import mysql.connector
login = int(input('1. Login, 2. Register, 3. Delete account::'))
username = input('username:')
password = input('password:')
conn_connect_to_server = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)


def database_creation_connection():
    pass


def register_account():
    try:
        cursor_accounts_database.execute(f'INSERT INTO account(username, password) VALUES (%s, %s)', (username, password))
        conn_connect_to_server.commit()
    except mysql.connector.errors.IntegrityError as a:
        print(f'Error username {username} already exists')


def login_account():
    cursor_accounts_database.execute('SELECT password FROM account WHERE username = %s', (username,))
    result_of_login = cursor_accounts_database.fetchone()

    if result_of_login:
        stored_password = result_of_login[0]
        if stored_password == password:
            print('Correct password')
        else:
            print('incorrect password')
    else:
        print('Username does not exist')


def delete_account():
    cursor_accounts_database.execute('SELECT 1 FROM account WHERE username = %s', (username,))
    result_account = cursor_accounts_database.fetchone()
    if result_account:
        cursor_accounts_database.execute('DELETE FROM account WHERE username = %s', (username,))
        print('account deleted')
    else:
        print('Such account doesnt exist')


cursor_accounts_database = conn_connect_to_server.cursor()
# Create a database 'accounts' where accounts would be stored with id, username, password
cursor_accounts_database.execute('CREATE DATABASE IF NOT EXISTS accounts')
conn_connect_to_server.database = 'accounts'
# Creates a table with colums ID, USERNAME, PASSWORD
cursor_accounts_database.execute('CREATE TABLE IF NOT EXISTS account (id INT PRIMARY KEY AUTO_INCREMENT, '
                                 'username VARCHAR(60) UNIQUE NOT NULL, '
                                 'password VARCHAR(60) NOT NULL)')
cursor_accounts_database.execute('CREATE TABLE IF NOT EXISTS account_phones (id INT, '
                                 'person VARCHAR(60) UNIQUE NOT NULL, '
                                 'phone_number INT NOT NULL,'
                                 'FOREIGN KEY (id) REFERENCES account(id))')
if login == 1:
    login_account()
elif login == 2:
    register_account()
elif login == 3:
    delete_account()


cursor_accounts_database.execute('SELECT * FROM account')
result = cursor_accounts_database.fetchall()
for table in result:
    print(table)