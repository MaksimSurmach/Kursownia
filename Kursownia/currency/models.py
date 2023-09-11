class Currency():
    '''
    Class representing currency.
    Currency has name and code.
    currency has buy and sell rates for other currencies.
    '''
    __exist_currencies = []
    def __init__(self, code: str, buy: float = None, sell: float = None, mid: float = None):
        self.code = code
        self.buy = buy
        self.sell = sell
        self.mid = mid
        self.can_be_updated = False

    def set_rate_currency(self, code: str, buy: float, sell: float):
        setattr(self, code, Currency(code, buy, sell))
        self.__exist_currencies.append(code)
        return True

    def update_currency(self, code: str, buy: float, sell: float):
        setattr(self, code, Currency(code, buy, sell))
        self.__exist_currencies.append(code)
        return True

    def get_currency(self, code: str):
        return getattr(self, code)

    def get_currency_code(self):
        return self.code

    def __str__(self):
        return f'{self.code}'

    def get_buy_rate(self, code: str):
        if code == self.code:
            return 1
        try:
            return getattr(self, code).buy
        except AttributeError:
            return None

    def get_sell_rate(self, code: str):
        if code == self.code:
            return 1
        try:
            return getattr(self, code).sell
        except AttributeError:
            return None

    def get_mid_rate(self, code: str):
        if code == self.code:
            return 1
        try:
            return getattr(self, code).mid
        except AttributeError:
            return None

    def enable_updated(self):
        setattr(self, "can_be_updated", True)
        return True

    def disable_updated(self):
        setattr(self, "can_be_updated", False)
        return False

    def get_all_rates(self):
        data = {}
        for currency in self.__exist_currencies:
            data[currency] = {
                'buy': self.get_buy_rate(currency),
                'sell': self.get_sell_rate(currency)
            }
        return data