from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
# Functions of the different options

# ___ Connect to DATABASE ___
conn_connect_to_server = sqlite3.connect('User_contact_database.sqlite')
cursor_accounts_database = conn_connect_to_server.cursor()
# ___ DATABASE FUNCTIONS ___

# ___ MESSAGE BOXES ___
current_user = None


def registration_complete():
    messagebox.showinfo(title='Registration', message='Your registration is complete!')


def registration_fail_user_exists():
    messagebox.showerror(title='User Exists', message='User already exists!')


def failed_login():
    messagebox.showerror(title='Error', message='Wrong username or password!')


def non_existent_user():
    messagebox.showerror(title='Error', message='Username does not exist!')


def delete_account_not_matching_passwords():
    messagebox.showerror(title='Error', message='Passwords do not match!')


def delete_account_incorrect_password():
    messagebox.showerror(title='Error', message='Wrong password!')


def delete_account_confirmation(account_deletion_password_input, account_deletion_password_confirm_input,
                                account_deletion_window):
    usable_account_deletion_password = account_deletion_password_input.get()
    usable_account_deletion_password_confirm = account_deletion_password_confirm_input.get()
    cursor_accounts_database.execute('SELECT password FROM account WHERE username = ?', (current_user,))
    password_check = cursor_accounts_database.fetchone()
    if usable_account_deletion_password == usable_account_deletion_password_confirm:
        if usable_account_deletion_password == password_check[0]:
            confirmation_delete_account_window = Toplevel()
            confirmation_delete_account_window.geometry('240x120')
            confirmation_delete_account_window.title('Deletion confirmation')
            confirmation_delete_account_window_label = Label(confirmation_delete_account_window,
                                                             text='Are you sure you want to delete your account?')
            confirmation_delete_account_button_yes = Button(confirmation_delete_account_window,
                                                            text='Yes',
                                                            command=lambda: delete_account(
                                                                confirmation_delete_account_window,
                                                                account_deletion_window))
            confirmation_delete_account_button_no = Button(confirmation_delete_account_window,
                                                           text='No',
                                                           command=lambda: confirmation_delete_account_window.destroy())

            confirmation_delete_account_window_label.pack()
            confirmation_delete_account_button_yes.pack()
            confirmation_delete_account_button_no.pack()
        else:
            delete_account_incorrect_password()
    else:
        delete_account_not_matching_passwords()


def account_login():
    global current_user
    usable_username_entry = login_username_entry.get()
    cursor_accounts_database.execute('SELECT password FROM account WHERE username = ?', (usable_username_entry,))
    result_of_login = cursor_accounts_database.fetchone()
    if result_of_login:
        stored_password = result_of_login[0]
        if stored_password == login_password_entry.get():
            current_user = usable_username_entry
            select_frame(account_frame)
            load_contacts_from_database()
        else:
            failed_login()
    else:
        non_existent_user()


def register_account():
    try:
        cursor_accounts_database.execute(f'INSERT INTO account(username, password) VALUES (?, ?)',
                                         (username_entry.get(), password_entry.get()))
        conn_connect_to_server.commit()
        registration_complete()
        select_frame(login_frame)
    except sqlite3.IntegrityError as a:
        registration_fail_user_exists()


def delete_account_window():
    """
    open a window that needs a password input, if it is correct, delete account and logout. Before deleting another
    windows pops up asking you are you sure and there are two an
    :return:
    """
    account_deletion_window = Toplevel()
    account_deletion_window.geometry('280x120')
    account_deletion_window.title('Account Deletion')
    account_deletion_password_label = Label(account_deletion_window,
                                            text='Password')
    account_deletion_password_confirm_label = Label(account_deletion_window,
                                                    text='Confirm Password')
    account_deletion_password_input = Entry(account_deletion_window)
    account_deletion_password_confirm_input = Entry(account_deletion_window)
    account_deletion_button = Button(account_deletion_window,
                                     command=lambda: delete_account_confirmation(
                                         account_deletion_password_input,
                                         account_deletion_password_confirm_input,
                                         account_deletion_window),
                                     text='DELETE')

    account_deletion_password_label.pack()
    account_deletion_password_input.pack()
    account_deletion_password_confirm_label.pack()
    account_deletion_password_confirm_input.pack()
    account_deletion_button.pack()


def delete_account(confirmation_delete_account_window, account_deletion_window):
    cursor_accounts_database.execute('DELETE FROM account WHERE username = ?', (current_user,))
    select_frame(login_frame)
    conn_connect_to_server.commit()
    # I have a problem with closing the windows after deleting the account
    if confirmation_delete_account_window.winfo_exists():
        confirmation_delete_account_window.destroy()
    if account_deletion_window.winfo_exists():
       account_deletion_window.destroy()


def change_password_window():
    """
    -check if passwords match with if
    """
    password_change_window = Toplevel()
    password_change_window.geometry('280x140')
    password_change_window.title('Password Change')
    current_password_label = Label(password_change_window,
                                   text='Current Password')
    current_password = Entry(password_change_window)
    confirm_password_label = Label(password_change_window,
                                   text='Confirm Password')
    confirm_password = Entry(password_change_window)
    new_password_label = Label(password_change_window,
                               text='New Password')
    new_password_entry = Entry(password_change_window)
    change_password_button = Button(password_change_window,
                                    text='Change Password',
                                    command=lambda: change_password(current_password,
                                                                    confirm_password,
                                                                    new_password_entry))
    current_password_label.pack()
    current_password.pack()
    confirm_password_label.pack()
    confirm_password.pack()
    new_password_label.pack()
    new_password_entry.pack()
    change_password_button.pack()


def change_password(current_password, confirm_password, new_password_entry):
    usable_current_password = current_password.get()
    usable_confirm_password = confirm_password.get()
    usable_new_password = new_password_entry.get()
    cursor_accounts_database.execute('UPDATE account SET password = ? WHERE username = ?', (usable_new_password,
                                                                                            current_user))
    conn_connect_to_server.commit()
    """
    -Write a if statements if passwords do not match
    -Make different error windows about it
    -If password match, change password and add a pop-up window saying that the password has been changed"""


def select_frame(frame):
    """Hide all frames and show only the selected one"""
    for f in (login_frame, sign_up_frame, account_frame):
        f.pack_forget()
    frame.pack(fill='both', expand=True)


def add_contact_to_database():
    """
    - Fetches unique user ID and gives it a variable
    - Inserts tree information into database, linking information with unique ID
    """
    cursor_accounts_database.execute('SELECT id FROM account WHERE username = ?', (current_user,))
    current_user_id = cursor_accounts_database.fetchone()
    name = name_box.get()
    last_name = lastname_box.get()
    number = number_box.get()
    cursor_accounts_database.execute(f'INSERT INTO account_phones(id, first_name, last_name, phone_number) '
                                     f'VALUES (?, ?, ?, ?)',
                                     (current_user_id[0], name, last_name, number))
    conn_connect_to_server.commit()
    load_contacts_from_database()
    name_box.delete(0, END)
    lastname_box.delete(0, END)
    number_box.delete(0, END)


def load_contacts_from_database():
    """
    - Deletes whole tree ,so it can load the database
    - Takes account ID and uses it to extract contact with that ID
    - Using a for_cycle display the contacts in the tree
    """
    for contact in my_tree.get_children():
        my_tree.delete(contact)
    cursor_accounts_database.execute(f'SELECT id FROM account WHERE username = ?',
                                     (current_user,))
    current_user_id = cursor_accounts_database.fetchone()

    cursor_accounts_database.execute(f'SELECT first_name, last_name, phone_number, id_contact '
                                     f'FROM account_phones WHERE id = ?',
                                     (current_user_id[0],))
    phone_book_data = cursor_accounts_database.fetchall()  # Contains the data in a tuple
    for row in phone_book_data:
        first_name, last_name, phone, id_contact = row
        my_tree.insert(parent='', index='end', iid=id_contact, text='Parent', values=(first_name, last_name, phone))


def remove_contact():
    delete_contacts = my_tree.selection()
    for record in delete_contacts:
        id_contact = record
        remove_contact_from_database(record)
        my_tree.delete(id_contact)


def remove_contact_from_database(id_contact):
    id_contact = int(id_contact)
    cursor_accounts_database.execute(f'DELETE FROM account_phones WHERE id_contact = ?', (id_contact, ))
    conn_connect_to_server.commit()


def log_out():
    global current_user
    select_frame(login_frame)
    current_user = None


#  App Window
app_window = Tk()
app_window.geometry('500x500')
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
                                   command=lambda: account_login())

login_button_menu_sign_up = Button(login_frame,
                                   text='Register',
                                   command=lambda: select_frame(sign_up_frame))
# runs first function with no argument, when clicked runs function with argument
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
                            text=f'Welcome {current_user}',
                            bd=13,
                            fg='#D9D02E',
                            font=('Ariel', 20, "bold"),
                            relief=RAISED,
                            padx=10,
                            pady=10,
                            bg='#6A2ED9'
                            )
button_add_contact_ac = Button(pack_buttons_left,
                               text='Add Contact',
                               command=lambda: add_contact_to_database()
                               )
button_delete_contact_ac = Button(pack_buttons_left,
                                  text='Delete Contact',
                                  command=lambda: remove_contact())
button_change_password_ac = Button(pack_buttons_left,
                                   command=lambda: change_password_window(),
                                   text='Change Password')

button_delete_account_ac = Button(pack_buttons_left,
                                  command=lambda: delete_account_window(),
                                  text='Delete Account')
button_logout_ac = Button(pack_buttons_left,
                          text='Logout',
                          command=lambda: log_out())
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
# ___ TREE COLUMNS ___
my_tree['columns'] = ('First name', 'Last name', 'PhoneNumber')

# ___TREE FORMAT COLUMNS___
my_tree.column('#0', width=0, stretch=NO)
my_tree.column('First name', anchor=W, width=80)
my_tree.column('Last name', anchor=CENTER, width=120)
my_tree.column('PhoneNumber', anchor=W, width=150)
# ___TREE CREATE HEADINGS___
my_tree.heading('#0', text='Label', anchor=W)
my_tree.heading('First name', text='First name', anchor=W)
my_tree.heading('Last name', text='Last name', anchor=CENTER)
my_tree.heading('PhoneNumber',text='PhoneNumber', anchor=W)
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
# ___ Account frame packs ___
account_title_label.pack()
button_add_contact_ac.pack(side='left', pady=10, padx=1)
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
# Making sure foreign keys work
cursor_accounts_database.execute("PRAGMA foreign_keys = ON;")
# Creates a table with columns ID, USERNAME, PASSWORD
cursor_accounts_database.execute('CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY AUTOINCREMENT, '
                                 'username VARCHAR(60) UNIQUE NOT NULL, '
                                 'password VARCHAR(60) NOT NULL)')
# Creates a table with columns, ID, First_name, last_name, phone_number
cursor_accounts_database.execute('CREATE TABLE IF NOT EXISTS account_phones ('
                                 'id INTEGER NOT NULL,'
                                 'id_contact INTEGER PRIMARY KEY AUTOINCREMENT, '
                                 'first_name VARCHAR(60) NOT NULL, '
                                 'last_name VARCHAR(60) NOT NULL, '
                                 'phone_number INT NOT NULL,'
                                 'FOREIGN KEY (id) REFERENCES account(id))')


select_frame(login_frame)
app_window.mainloop()
