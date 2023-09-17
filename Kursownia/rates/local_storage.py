import Kursownia.rates.rate_getter as rate_getter
from Kursownia.currency.models import Currency

class Storage():
    def __init__(self):
        self.currencies = ['EUR', 'USD', 'PLN', 'BYN']
        self.updated_currencies = ['PLN', 'BYN', 'EUR']
        for currency in self.currencies:
            setattr(self, currency, Currency(currency))
        # self.update_rates()

    async def update_rates(self):
        print('Updating rates')
        for currency in self.updated_currencies:
            if currency == 'PLN':
                try:
                    uero = rate_getter.request_pln_euro_rate()
                    dollar = rate_getter.request_pln_dollar_rate()
                except Exception as e:
                    print(f"Error while updating rates {currency}")
                    print(e)
                    continue
                getattr(self, 'PLN').set_rate('EUR', 1/uero['sell'])
                getattr(self, 'PLN').set_rate('USD', 1/dollar['sell'])
                getattr(self, 'EUR').set_rate('PLN', uero['buy'])
                getattr(self, 'USD').set_rate('PLN', dollar['buy'])
            elif currency == 'BYN':
                try:
                    data = rate_getter.request_BYN_rates()
                except Exception as e:
                    print(f"Error while updating rates {currency}")
                    print(e)
                    continue
                for cur in data:
                    getattr(self, 'BYN').set_rate(cur, 1/data[cur]['buy'])
                    getattr(self, cur).set_rate('BYN', data[cur]['sell'])

            elif currency == 'EUR':
                try:
                    data = rate_getter.get_croos_rates()
                except Exception as e:
                    print(f"Error while updating rates {currency}")
                    print(e)
                    continue
                getattr(self, 'EUR').set_rate('USD', data['USD'])
                getattr(self, 'USD').set_rate('EUR', 1/data['EUR'])
        return True

    def get_rate(self, sold_code: str, bought_code: str):
        return getattr(self, sold_code).get_rate(bought_code)

    def get_currency(self, code: str):
        return getattr(self, code)

    def calculate(self, sold_code: str, bought_code: str, amount: float):
        return getattr(self, sold_code).calc_rate(bought_code, amount)







