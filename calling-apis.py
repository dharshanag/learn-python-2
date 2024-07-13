import requests

response = requests.get('https://open.er-api.com/v6/latest/USD')
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")



def get_exchange_rate(currency_code):
    # Retrieve the exchange rate for the given currency code
    rates = data['rates']
    return rates.get(currency_code, 'Currency code not found')



response = requests.get('https://open.er-api.com/v6/latest/USD')
if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to retrieve data: {response.status_code}")


currency_code = input("Please input a three letter abbreviation for any country and you will be given the exchange rate to US dollars: ")
exchange_rate = get_exchange_rate(currency_code)
print(f"The exchange rate for {currency_code} is {exchange_rate}")
