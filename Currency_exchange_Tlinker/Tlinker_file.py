# import requests
#
# def convert_currency(amount, base_currency, target_currency):
#     url = f"https://moneymorph.dev/api/convert/{amount}/{base_currency}/{target_currency}"
#     response = requests.get(url)
#     data = response.json()
#
#     result = data['response']
#     print(f"{amount} {base_currency} = {result:.2f} {target_currency}")
#
#
# # Example
# convert_currency(109, 'JPY', 'BGN')

from tkinter import *

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")  # changes size of window
window.title("Currency exchange program")

icon = PhotoImage(file='currency_exchange_logo.png')  # Converts image to 'PhotoImage' that the tkinter can use
window.iconphoto(True, icon)  # Function that can use the photoimage
window.config(background='black')  # changes background colour, can use hex value

label = Label(window,
              text='Hello world maybesss?',
              font=('Arial',40,'bold'),
              fg='green',
              bg='red',
              relief=RAISED, # Setting type of border
              bd=10,    # Border width
              padx=20,  # Space right and left of border
              pady=20,  # Space top and bottom of border
              image=icon,  # Placing image into the label
              compound='bottom')
# Creates a label, an area widget that hold text or image within a window
#  Default label, lebel.pack()
label.place(x=0,y=0)
def click():
    print("Button clicked")
button = Button(window,
                text="Click me",
                command=click,
                font=("Comic Sans", 30),
                fg="White",
                bg='Black',
                activebackground='Black',
                activeforeground='White')
button.pack()

window.mainloop()  # places window on screen and listens to events