from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
# Functions of the different options

# ___ Connect to DATABASE ___
conn_connect_to_server = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456'
)
cursor_accounts_database = conn_connect_to_server.cursor()

# ___ DATABASE FUNCTIONS ___

# ___ MESSAGE BOXES ___
current_user_id = None


def failed_login():
    messagebox.showerror(title='Error', message='Wrong username or password!')


def non_existent_user():
    messagebox.showerror(title='Error', message='Username does not exist!')


def account_login():
    global current_user_id
    usable_username_entry = login_username_entry.get()
    cursor_accounts_database.execute('SELECT password FROM account WHERE username = %s', (usable_username_entry,))
    result_of_login = cursor_accounts_database.fetchone()
    if result_of_login:
        stored_password = result_of_login[0]
        if stored_password == login_password_entry.get():
            current_user_id = usable_username_entry
            select_frame(account_frame)
        else:
            failed_login()
    else:
        non_existent_user()


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
        print('Such an account doesnt exist')


def select_frame(frame):
    """Hide all frames and show only the selected one"""
    for f in (login_frame, sign_up_frame, account_frame):
        f.pack_forget()
    frame.pack(fill='both', expand=True)


def add_contact():
    global index_count
    my_tree.insert(parent='', index='end', iid=index_count, text='Parent',
                   values=(name_box.get(), lastname_box.get(), number_box.get()))
    name_box.delete(0, END)
    lastname_box.delete(0, END)
    number_box.delete(0, END)
    index_count += 1

def remove_conract():
    delete_contact = my_tree.selection()
    for record in delete_contact:
        my_tree.delete(record)


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
                                   text='Sign in',
                                   command=lambda:account_login())

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

# ___ACCOUNT FRAME___
account_frame = Frame(app_window, background='#9431ce')
pack_buttons_left = Frame(account_frame, background='#9431ce')
contact_management_frame = Frame(account_frame)
account_title_label = Label(account_frame,
                    text=f'Welcome {current_user_id}',
                    bd=13,
                    fg='#D9D02E',
                    font=('Ariel', 20, "bold"),
                    relief=RAISED,
                    padx=10,
                    pady=10,
                    bg='#6A2ED9'
                    )
button_browse_contacts_ac = Button(pack_buttons_left,
                                   text='Add Contact',
                                   command=lambda: add_contact()
                                   )
button_change_password_ac = Button(pack_buttons_left,
                                   text='Change Password')
button_delete_contact_ac = Button(pack_buttons_left,
                                  text='Delete Contact',
                                  command=lambda: remove_conract())
button_delete_account_ac = Button(pack_buttons_left,
                             text='Delete Account')
button_logout_ac = Button(pack_buttons_left,
                             text='Logout')
# ___CONTACT MANAGEMENT___
# Labels
contact_name = Label(contact_management_frame, text='Name')
contact_last_name = Label(contact_management_frame, text='Last Name')
contact_number = Label(contact_management_frame, text='Number')
# Entry boxes
name_box = Entry(contact_management_frame)
lastname_box = Entry(contact_management_frame)
number_box = Entry(contact_management_frame)

# ___ TREE ___
my_tree = ttk.Treeview(account_frame)
#___ TREE COLUMS ___
my_tree['columns'] = ('First name', 'Last name', 'PhoneNumber')
global index_count
index_count = 0

#___TREE FORMAT COLUMS___
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('First name', anchor=W, width=80)
my_tree.column('Last name', anchor=CENTER, width=120)
my_tree.column('PhoneNumber', anchor=W, width=150)
# ___TREE CREATE HEADINGS___
my_tree.heading('#0', text='Label', anchor=W)
my_tree.heading('First name', text='First name', anchor=W)
my_tree.heading('Last name', text='Last name', anchor=CENTER)

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
# ___packs___
account_title_label.pack()
button_browse_contacts_ac.pack(side='left', pady=10, padx=1)
button_delete_contact_ac.pack(side='left', pady=10, padx=1)
button_change_password_ac.pack(side='left', pady=10, padx=1)
button_delete_account_ac.pack(side='left', pady=10, padx=1)
button_logout_ac.pack(side='left', pady=10, padx=1)
# contact management
contact_name.grid(row=0, column=0)
contact_last_name.grid(row=0, column=1)
contact_number.grid(row=0, column=2)
name_box.grid(row=1, column=0)
lastname_box.grid(row=1, column=1)
number_box.grid(row=1, column=2)

account_frame.pack(fill='both', expand=True)
pack_buttons_left.pack(padx=20)
contact_management_frame.pack(pady=20)
my_tree.pack()

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
#test