import Kursownia.rates.rate_getter as rate_getter
from Kursownia.currency.models import Currency

class Storage():
    def __init__(self):
        self.currencies = ['EUR', 'USD', 'PLN', 'BLR']
        self.updated_currencies = ['PLN', 'BLR', 'EUR']
        for currency in self.currencies:
            setattr(self, currency, Currency(currency))
        self.update_rates()

    def update_rates(self):
        for currency in self.updated_currencies:
            if currency == 'PLN':
                uero = rate_getter.request_pln_euro_rate()
                dollar = rate_getter.request_pln_dollar_rate()
                getattr(self, currency).update_currency('EUR', uero['buy'], uero['sell'])
                getattr(self, currency).update_currency('USD', dollar['buy'], dollar['sell'])
                getattr(self, 'USD').update_currency('PLN', dollar['sell'], dollar['buy'])
                getattr(self, 'EUR').update_currency('PLN', uero['sell'], uero['buy'])
            elif currency == 'BLR':
                data = rate_getter.request_blr_rates()
                for cur in data:
                    getattr(self, 'BLR').update_currency(data[cur]['code'], data[cur]['buy'], data[cur]['sell'])
                    getattr(self, data[cur]['code']).update_currency(currency, data[cur]['sell'], data[cur]['buy'])
            elif currency == 'EUR':
                data = rate_getter.get_croos_rates()
                getattr(self, 'EUR').update_currency('USD', data['USD'], data['EUR'])
                getattr(self, 'USD').update_currency('EUR', data['EUR'], data['USD'])

        return True

    def get_rate(self, sold_code: str, bought_code: str):
        return getattr(self, sold_code).get_buy_rate(bought_code)

    def get_currency(self, code: str):
        return getattr(self, code)

    def get_currency_code(self, code: str):
        return getattr(self, code).get_currency_code()

    def get_buy_rate(self, sold_code: str, bought_code: str):
        return getattr(self, sold_code).get_buy_rate(bought_code)

    def get_sell_rate(self, sold_code: str, bought_code: str):
        return getattr(self, sold_code).get_sell_rate(bought_code)







