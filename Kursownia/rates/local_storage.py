import Kursownia.rates.rate_getter as rate_getter
from Kursownia.currency.models import Currency


class Storage():
    def __init__(self):
        self.currencies = ['EUR', 'USD', 'PLN', 'BYN'] # List of currencies
        self.updated_currencies = ['PLN', 'BYN', 'EUR'] # List of currencies that need to be updated
        # Create currency objects for each currency
        for currency in self.currencies:
            setattr(self, currency, Currency(currency))

    async def update_rates(self):
        print('Updating rates')
        for currency in self.updated_currencies:
            if currency == 'PLN':
                try:
                    # Get rates from NBP
                    euro = rate_getter.request_pln_euro_rate()
                    dollar = rate_getter.request_pln_dollar_rate()
                except Exception as e:
                    # if any error occurs, skip this currency
                    print(f"Error while updating rates {currency}")
                    print(e)
                    continue
                # Set rates for each currency
                getattr(self, 'PLN').set_rate('EUR', 1 / euro['sell'])
                getattr(self, 'PLN').set_rate('USD', 1 / dollar['sell'])
                getattr(self, 'EUR').set_rate('PLN', euro['buy'])
                getattr(self, 'USD').set_rate('PLN', dollar['buy'])
            elif currency == 'BYN':
                try:
                    data = rate_getter.request_BYN_rates()
                except Exception as e:
                    # if any error occurs, skip this currency
                    print(f"Error while updating rates {currency}")
                    print(e)
                    continue
                for cur in data:
                    # Set rates for each currency
                    getattr(self, 'BYN').set_rate(cur, 1 / data[cur]['buy'])
                    getattr(self, cur).set_rate('BYN', data[cur]['sell'])

            elif currency == 'EUR':
                try:
                    data = rate_getter.get_crosshatches()
                except Exception as e:
                    # if any error occurs, skip this currency
                    print(f"Error while updating rates {currency}")
                    print(e)
                    continue
                # Set rates for each currency
                getattr(self, 'EUR').set_rate('USD', data['USD'])
                getattr(self, 'USD').set_rate('EUR', 1 / data['EUR'])
        # anyway, return True
        return True

    def calculate(self, sold_code: str, bought_code: str, amount: float):
        # send command 'calc_rate' to the currency object with sold_code
        return getattr(self, sold_code).calc_rate(bought_code, amount)
