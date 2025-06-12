import requests


def external_currency_extraction():
    pass


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
    print('Base currency:')
    print('1. Euro 2. Australian Dollar 3. Bulgarian Lev 4. Japanese Yen')
    base_currency_raw_input = int(input('Convert currency from: '))
    print('Target currency:')
    print('1. Euro 2. Dollar 3. Bulgarian Lev 4. Japanese Yen')
    target_currency_raw_input = int(input('Convert currency into: '))
    amount = input('Amount: ')
    base_currency, target_currency = option_1_currency_to_json(base_currency_raw_input, target_currency_raw_input)

    converted_currency = currency_conversion(amount, base_currency, target_currency)
    return f'{amount} {base_currency} = {converted_currency:.2f} {target_currency}'


def option_1_currency_to_json(base_currency_raw_input, target_currency_raw_input):
    """
    - Function receives the option the user wants as an integer
    - Converts those integers to strings that can be used by the request URL
    """
    if base_currency_raw_input == 1:
        base_currency = 'EUR'
    elif base_currency_raw_input == 2:
        base_currency = 'AUD'
    elif base_currency_raw_input == 3:
        base_currency = 'BGN'
    elif base_currency_raw_input == 4:
        base_currency = 'JPY'

    if target_currency_raw_input == 1:
        target_currency = 'EUR'
    elif target_currency_raw_input == 2:
        target_currency = 'AUD'
    elif target_currency_raw_input == 3:
        target_currency = 'BGN'
    elif target_currency_raw_input == 4:
        target_currency = 'JPY'

    return base_currency, target_currency



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
        returned_option_1 = option_1()
        print(returned_option_1)
    elif option_input == 2:
        pass
    elif option_input == 3:
        pass
    elif option_input == 4:
        pass
    pass

menu()