from tkinter import *
# Functions of the different options


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
                             text='Sign up',
                             command=lambda:select_frame(sign_up_frame)) # runs first function with no argument, when clicked runs function with argument
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
                             text='Sign in')

button_menu_sign_up = Button(sign_up_frame,
                             text='Sign up')


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

select_frame(login_frame)
app_window.mainloop()