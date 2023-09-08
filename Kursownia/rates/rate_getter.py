import requests


def request_euro_rate():
    response = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json')
    return response.json()['rates'][0]['mid']

def request_dollar_rate():
    response = requests.get('http://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json')
    return response.json()['rates'][0]['mid']




