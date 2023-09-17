class Currency():
    """
    Class representing currency.
    Currency has name and code.
    currency has buy and sell rates for other currencies.
    """
    __exist_currencies = []

    def __init__(self, code: str):
        self.code = code

    def get_currency_code(self):
        return self.code

    def __str__(self):
        return f'{self.code}'

    def set_rate(self, code: str, buy: float):
        buy = float(buy)
        if buy < 0:
            raise ValueError('Rate cannot be negative')
        if buy == 0:
            raise ValueError('Rate cannot be zero')
        # convert to float
        setattr(self, code, buy)

    def get_rate(self, code: str):
        return getattr(self, code)

    def calc_rate(self, code: str, amount: float):
        return round(amount * self.get_rate(code), 2)
