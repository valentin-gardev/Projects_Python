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

window = Tk() # instantiate an instance of a window
window.geometry("420x420") # changes size of window
window.title("Currency exchange program")

icon = PhotoImage(file='currency_exchange_logo.png')  # Converts image to 'PhotoImage' that the tkinter can use
window.iconphoto(True, icon) # Function that can use the photoimage
window.config(background='black') # changes background colour, can use hex value

window.mainloop()  # places window on screen and listens to events