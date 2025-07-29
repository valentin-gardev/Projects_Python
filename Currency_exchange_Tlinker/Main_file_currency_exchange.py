from tkinter import *
import mysql.connector
# Functions of the different options

# ___ Connect to DATABASE ___
conn_connect_to_server = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)
cursor_accounts_database = conn_connect_to_server.cursor()

# ___ DATABASE FUNCTIONS ___


def register_account():
    try:
        cursor_accounts_database.execute(f'INSERT INTO account(username, password) VALUES (%s, %s)', (username_entry.get(), password_entry.get()))
        conn_connect_to_server.commit()
    except mysql.connector.errors.IntegrityError as a:
        print(f'Error username {username_entry} already exists')


def delete_account():
    cursor_accounts_database.execute('SELECT 1 FROM account WHERE username = %s', (login_username_entry.get(),))
    result_account = cursor_accounts_database.fetchone()
    if result_account:
        cursor_accounts_database.execute('DELETE FROM account WHERE username = %s', (login_username_entry.get(),))
        print('account deleted')
    else:
        print('Such account doesnt exist')


def select_frame(frame):
    """Hide all frames and show only the selected one"""
    for f in (login_frame, sign_up_frame):
        f.pack_forget()
    frame.pack(fill='both', expand=True)


#  App Window
app_window = Tk()
app_window.geometry('420x420')
app_window.title('Main Menu')
app_window.config()

# ___ Frames ___
login_frame = Frame(app_window, background='#9431ce')
sign_up_frame = Frame(app_window, background='#9431ce')
account_frame = Frame(app_window, background='#9431ce')

# ___ Login Frame ___
login_title_label = Label(login_frame,
                          text='Log in',
                          bd=13,
                          fg='#D9D02E',
                          font=('Ariel', 20, "bold"),
                          relief=RAISED,
                          padx=10,
                          pady=10,
                          bg='#6A2ED9'
                          )
login_username_label = Label(login_frame,
                             text='Username',
                             background='#9431ce')
login_username_entry = Entry(login_frame,
                       )
login_password_label = Label(login_frame,
                             text='Password',
                             background='#9431ce')
login_password_entry = Entry(login_frame,
                       )
login_button_menu_sign_in = Button(login_frame,
                                   text='Sign in')

login_button_menu_sign_up = Button(login_frame,
                                   text='Register',
                                   command=lambda: select_frame(sign_up_frame)) # runs first function with no argument, when clicked runs function with argument
# ___ Sign up Frame ___
title_label = Label(sign_up_frame,
                    text='Create an Account',
                    bd=13,
                    fg='#D9D02E',
                    font=('Ariel', 20, "bold"),
                    relief=RAISED,
                    padx=10,
                    pady=10,
                    bg='#6A2ED9'
                    )
username_label = Label(sign_up_frame,
                       text='Username',
                       background='#9431ce')
username_entry = Entry(sign_up_frame,
                       )
password_label = Label(sign_up_frame,
                       text='Password',
                       background='#9431ce')
password_entry = Entry(sign_up_frame,
                       )
button_menu_sign_in = Button(sign_up_frame,
                             text='Sign in',
                             command=lambda: select_frame(login_frame))

button_menu_sign_up = Button(sign_up_frame,
                             text='Register account',
                             command=lambda: register_account())
# ___ Account frame ___
account_title_label = Label(account_frame,
                    text='Welcome (name of account)',
                    bd=13,
                    fg='#D9D02E',
                    font=('Ariel', 20, "bold"),
                    relief=RAISED,
                    padx=10,
                    pady=10,
                    bg='#6A2ED9'
                    )
button_browse_contacts_ac = Button(account_frame,
                             text='Browse Contacts')
button_change_password_ac = Button(account_frame,
                             text='Change Password')
button_delete_account_ac = Button(account_frame,
                             text='Delete Account')
# ___ Login frame pack ___

login_title_label.pack()
login_username_label.pack()
login_username_entry.pack()
login_password_label.pack()
login_password_entry.pack()
login_button_menu_sign_in.pack(pady=5)
login_button_menu_sign_up.pack()

# ___ Sign up frame pack ___
title_label.pack()
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
button_menu_sign_up.pack(pady=5)
button_menu_sign_in.pack()
# ___ Account frame pack ___
account_title_label.pack()
button_delete_account_ac.pack()
button_change_password_ac.pack()
button_browse_contacts_ac.pack()

# ___ DataBase Creation ___
# Create a database 'accounts' where accounts would be stored with id, username, password
cursor_accounts_database.execute('CREATE DATABASE IF NOT EXISTS accounts')
conn_connect_to_server.database = 'accounts'
# Creates a table with columns ID, USERNAME, PASSWORD
cursor_accounts_database.execute('CREATE TABLE IF NOT EXISTS account (id INT PRIMARY KEY AUTO_INCREMENT, '
                                 'username VARCHAR(60) UNIQUE NOT NULL, '
                                 'password VARCHAR(60) NOT NULL)')
cursor_accounts_database.execute('CREATE TABLE IF NOT EXISTS account_phones (id INT, '
                                 'person VARCHAR(60) UNIQUE NOT NULL, '
                                 'phone_number INT NOT NULL,'
                                 'FOREIGN KEY (id) REFERENCES account(id))')


select_frame(login_frame)
app_window.mainloop()