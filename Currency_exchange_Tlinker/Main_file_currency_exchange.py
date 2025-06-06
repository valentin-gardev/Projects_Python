import requests


def external_currency_extraction():
    pass


def currency_conversion(amount: int, base_currency: int, target_currency: int):
    url = f"https://moneymorph.dev/api/convert/{amount}/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    if 'result' in data:
        result = data['response']
        return result
    else:
        return 'Result not available in response!'


def show_live_currency_values():
    pass


def check_if_int(choice_menu=None, choice_currency_conversion=None):
    """
    Checks if needed input is an integer, if not, prints appropriate response
    """
    if choice_menu is not None:
        while True:
            try:
                choice_menu = int(choice_menu)
                if choice_menu not in (1, 2, 3, 4):
                    choice_menu = input('Invalid number! Please choose between options 1, 2, 3, 4:')
                else:
                    return choice_menu

            except ValueError:
                choice_menu = input('Invalid input! Please choose a number between 1, 2, 3, 4:')
    if choice_currency_conversion is not None:
        while True:
            try:
                is_int_choice_currency_conversion = int(choice_currency_conversion)
                if is_int_choice_currency_conversion not in (1, 2, 3, 4):
                    choice_currency_conversion = input('Invalid option.')
            
            except ValueError:
                pass
                
    pass

# Different options are their own functions
def option_1():
    print('1. Euro 2. Dollar 3. Bulgarian Lev 4. Japanese Yen')
    base_currency = input('Convert currency from: ')
    print('1. Euro 2. Dollar 3. Bulgarian Lev 4. Japanese Yen')
    target_currency = input('Convert currency into: ')
    amount = input('Amount: ')
    converted_currency = currency_conversion(amount, base_currency, target_currency)


def menu():
    """
    Menu inputs for selecting currencies:
    """
    print('Welcome to the currency exchange information program')
    print('Please choose an option:')
    print('1. Convert currency')
    option_input = input()
    option_input = check_if_int(choice_menu=option_input)

    if option_input == 1:
        option_1()
    elif option_input == 2:
        pass
    elif option_input == 3:
        pass
    elif option_input == 4:
        pass
    pass

menu()