class Currency:
    """
    Class representing currency.
    Currency has name and code.
    currency has buy and sell rates for other currencies.
    """
    __exist_currencies = []

    def __init__(self, code: str):
        # create currency object by code
        self.code = code

    def __str__(self):
        # when printing object, print code
        return f'{self.code}'

    def set_rate(self, code: str, buy: float):
        # set rate for currency
        buy = float(buy)  # convert to float
        if buy < 0:
            raise ValueError('Rate cannot be negative')
        if buy == 0:
            raise ValueError('Rate cannot be zero')
        setattr(self, code, buy)

    def get_rate(self, code: str):
        # get rate for currency by code
        return getattr(self, code)

    def calc_rate(self, code: str, amount: float):
        # calculate rate for currency by code and limit to 2 decimal places
        return round(amount * self.get_rate(code), 2)
