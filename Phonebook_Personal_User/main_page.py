from tkinter import *
#  Main menu
main_menu_window = Tk()
main_menu_window.geometry('420x420')
main_menu_window.title('Main Menu')
main_menu_window.config(background='#9431ce')
# Main menu Label
menu_label = Label(main_menu_window,
                   text='Main Menu',
                   bd=13,
                   fg='#D9D02E',
                   font=('Ariel', 20, "bold"),
                   relief=RAISED,
                   padx=10,
                   pady=10,
                   bg='#6A2ED9'
                   )

# GUI packs
menu_label.pack()
main_menu_window.mainloop()

