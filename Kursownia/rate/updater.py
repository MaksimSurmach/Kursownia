from typing import Any
import requests
import json


def request_from_bank():
    '''
    Get exchange rate from bank
    '''
    # обернем в try,catch. усли у нас будет ошибка Exception то выведем на экран и вернем false
    try:
        request = requests.get("https://api.nbp.pl/api/exchangerates/tables/C?format=json")
        # get send http request to bank
    except Exception as error:
        print(error)
        return False
    
    # serialize income information to json
    data = request.json()

    return data[0]  #[0] because this is bank style


def find_euro(data):
    # lets find euro in response

    # thats like answer type
    answer = {"cur": "EUR", "buy": 0, "sold": 0} 

    for cur in data.get("rates", []):
        # iterate in rate array
        ''' example of income date where we search euro
        {
            "currency": "dolar amerykański",
            "code": "USD",
            "bid": 4.0873,
            "ask": 4.1699
        }
        '''
        # check if in "code" value has EUR symbols
        # can use just "EUR" == cur.get("code")
        if "EUR" in cur.get("code"):
            answer["buy"] = cur.get("bid")
            answer["sold"] = cur.get("ask")
            return answer
            # return if find euro
        
    # anyway return something
    return answer

def get_euro_rate() -> dict:

    # call function for get data from bank api
    bank_api = request_from_bank()

    if bank_api is False:
        # failed get from api,
        return {"error": "Failed get from api"}

    #need to find euro in data
    euro = find_euro(bank_api)

    return euro


if __name__ == "__main__":
    print(get_euro_rate())

