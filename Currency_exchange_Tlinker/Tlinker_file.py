from tkinter import *


currency_exchange_window = Tk()
currency_exchange_window.geometry('420x240')
currency_exchange_window.title("Currency exchange program")
window_icon = PhotoImage(file='currency_exchange_logo.png')  # Converts image to 'PhotoImage' that the tkinter can use
currency_exchange_window.iconphoto(True, window_icon)  # Function that can use the photoimage
# LABEL title
label_program = Label(currency_exchange_window,
                      text='Currency Converter',
                      bd=13,
                      fg='red',
                      font=('Ariel', 25, "bold"),
                      relief=RAISED,
                      padx=10,
                      pady=10
                      )
# LABEL from / to currencies
label_currency_from = Label(currency_exchange_window,
                            text='From:')
label_currency_to = Label(currency_exchange_window,
                          text='To:')
# RADIO BUTTONS options to convert FROM
available_currencies = ['EUR', 'AUD', 'BGN', 'JPY']
select_from = IntVar()
frame_currency_buttons_from = Frame(currency_exchange_window)  # Creating a frame of the currency radio buttons from
for currency in range(len(available_currencies)):
    radio_button_currencies_from = Radiobutton(frame_currency_buttons_from, text=available_currencies[currency], variable=select_from, value=currency)
    radio_button_currencies_from.pack(side='left')

# RADIO BUTTONS options to convert TO
available_currencies = ['EUR', 'AUD', 'BGN', 'JPY']
select_to = IntVar()
frame_currency_buttons_to = Frame(currency_exchange_window)  # Creating a frame of the currency radio buttons to
for currency in range(len(available_currencies)):
    radio_button_currencies_to = Radiobutton(frame_currency_buttons_to, text=available_currencies[currency], variable=select_to, value=currency)
    radio_button_currencies_to.pack(side='left')


# LABEL and TEXT for amount
currency_amount = Label(currency_exchange_window,
                        text='Amount:')
text = Text(currency_exchange_window, height= 5, width= 50)

# Conversion BUTTON

conversion_button = Button()
label_program.pack()
label_currency_from.pack()
frame_currency_buttons_from.pack()
label_currency_to.pack()
frame_currency_buttons_to.pack()
currency_amount.pack()
text.pack()
currency_exchange_window.mainloop()