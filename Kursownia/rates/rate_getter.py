import requests
import xmltodict


def request_pln_euro_rate():
    # send request to NBP API
    response = requests.get('http://api.nbp.pl/api/exchangerates/rates/c/eur/?format=json')
    # return dictionary with currency data
    return {
        'name': response.json()['currency'],
        'code': response.json()['code'],
        'buy': float(response.json()['rates'][0]['bid']),
        'sell': float(response.json()['rates'][0]['ask'])
    }


def request_pln_dollar_rate():
    # send request to NBP API
    response = requests.get('http://api.nbp.pl/api/exchangerates/rates/c/usd/?format=json')
    return {
        'name': response.json()['currency'],
        'code': response.json()['code'],
        'buy': float(response.json()['rates'][0]['bid']),
        'sell': float(response.json()['rates'][0]['ask'])
    }


def request_byn_rates():
    # send request to NBRB API
    response = requests.get('https://belapb.by/CashExRatesDaily.php')
    # convert xml to dictionary
    response = xmltodict.parse(response.text)
    data = {}
    # iterate over all currencies and add them to dictionary
    for currency in response['DailyExRates']['Currency']:
        if currency['CharCode'] in ('USD', 'EUR', 'PLN'):
            data[currency['CharCode']] = {
                'code': currency['CharCode'],
                'name': currency['Name'],
                'buy': float(currency['RateBuy']) / float(currency['Scale']),
                'sell': float(currency['RateSell']) / float(currency['Scale'])
            }
    return data


def get_crosshatches():
    # send request to AlfaBank API
    response = requests.get('https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates')
    response = response.json()
    data = {}
    # iterate over all currencies and add them to dictionary
    for currency in response['rates']:
        if currency['sellIso'] == 'EUR' and currency['buyIso'] == 'USD':
            data[currency['sellIso']] = float(currency['sellRate'])
            data[currency['buyIso']] = float(currency['buyRate'])
    return data
