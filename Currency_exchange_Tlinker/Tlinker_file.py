import requests

def convert_currency(amount, base_currency, target_currency):
    url = f"https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()
    result = data['result']
    print(f"{amount} {base_currency} = {result:.2f} {target_currency}")

# Example
convert_currency(100, 'INR', 'JPY')
convert_currency(250, 'GBP', 'CAD')