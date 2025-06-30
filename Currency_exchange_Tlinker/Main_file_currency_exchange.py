from tkinter import *
import requests


def currency_conversion(amount: int, base_currency: str, target_currency: str):
    """
     _ Website used for free currency exchange ratios https://moneymorph.dev
     - URL showing all the available currencies https://moneymorph.dev/api/currencies
    """
    url = f"https://moneymorph.dev/api/convert/{amount}/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    result = data['response']
    return result


def clicked_conversion_button():
    """
    Conversion button is clicked:
    - gets the two radio button selections(from/to)
    - calls function checking if the Amount text given is a string
    - calls currency_conversion_api function that converts the given amount from x to y currency
    - updates the converted currency label
    """
    selected_from = select_from.get()
    selected_to = select_to.get()
    amount_put_for_conversion = check_if_string()
    converted_amount = currency_conversion(amount_put_for_conversion, selected_from, selected_to)
    label_converted_currency.config(text=converted_amount)


def check_if_string():  # Check if the input amount text is an integer
    amount_input = text_amount_input.get('1.0', END)
    try:
        amount_input = int(amount_input)
        return amount_input
    except:
        amount_input = str(amount_input)
        label_converted_currency.config(text='Please input a natural number')
# def test_print()

currency_exchange_window = Tk()
currency_exchange_window.geometry('420x320')
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
select_from = StringVar()
frame_currency_buttons_from = Frame(currency_exchange_window)  # Creating a frame of the currency radio buttons from
for currency in available_currencies:
    radio_button_currencies_from = Radiobutton(frame_currency_buttons_from,
                                               text=currency,
                                               variable=select_from,
                                               value=currency,
                                               )
    radio_button_currencies_from.pack(side='left')

select_from.set('EUR')  # Setting the starting selected button with the index
# RADIO BUTTONS options to convert TO
available_currencies = ['EUR', 'AUD', 'BGN', 'JPY']
select_to = StringVar()

frame_currency_buttons_to = Frame(currency_exchange_window)  # Creating a frame of the currency radio buttons to
for currency in available_currencies:
    radio_button_currencies_to = Radiobutton(frame_currency_buttons_to,
                                             text=currency,
                                             variable=select_to,
                                             value=currency,
                                             )
    radio_button_currencies_to.pack(side='left')
select_to.set('EUR')

# LABEL and TEXT for amount
currency_amount = Label(currency_exchange_window,
                        text='Amount:')
text_amount_input = Text(currency_exchange_window,
            height=1,
            width=10,
            )

# Conversion BUTTON
# Check if the Amount label is a string or float, if it is string, print message, output a message box if it is not int

conversion_button = Button(currency_exchange_window,
                           text='Convert',
                           command=clicked_conversion_button,
                           )

label_converted_currency = Label(currency_exchange_window,
                   text='')
label_program.pack()
label_currency_from.pack()
frame_currency_buttons_from.pack()
label_currency_to.pack()
frame_currency_buttons_to.pack()
currency_amount.pack()
text_amount_input.pack()
conversion_button.pack()
label_converted_currency.pack()
currency_exchange_window.mainloop()