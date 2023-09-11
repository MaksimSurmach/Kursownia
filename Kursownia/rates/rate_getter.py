import requests
import xmltodict

def request_pln_euro_rate():
    response = requests.get('http://api.nbp.pl/api/exchangerates/rates/c/eur/today/?format=json')
    return {
        'name': response.json()['currency'],
        'code': response.json()['code'],
        'buy': response.json()['rates'][0]['bid'],
        'sell': response.json()['rates'][0]['ask']
    }

def request_pln_dollar_rate():
    response = requests.get('http://api.nbp.pl/api/exchangerates/rates/c/usd/today/?format=json')
    return {
        'name': response.json()['currency'],
        'code': response.json()['code'],
        'buy': response.json()['rates'][0]['bid'],
        'sell': response.json()['rates'][0]['ask']
    }

def request_blr_rates():
    response = requests.get('https://belapb.by/CashExRatesDaily.php')
    response = xmltodict.parse(response.text)
    data = {}
    for currency in response['DailyExRates']['Currency']:
        if currency['CharCode'] in ('USD', 'EUR', 'PLN'):
            data[currency['CharCode']] = {
                'code': currency['CharCode'],
                'name': currency['Name'],
                'buy': currency['RateBuy'],
                'sell': currency['RateSell']
            }
    return data


def get_croos_rates():
    response = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
    response = response.json()
    data = {}
    for currency in response['rates']:
        if currency['sellIso'] == 'EUR' and currency['buyIso'] == 'USD':
            data[currency['sellIso']] = currency['sellRate']
            data[currency['buyIso']] = currency['buyRate']

    return data




