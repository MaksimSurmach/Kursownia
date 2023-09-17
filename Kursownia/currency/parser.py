import string


class TextToCurrencyParser:
    __keywords = {
        'USD': ['USD', 'dollar', 'dollars', 'usd', 'dolar', 'dolara', 'dolary', 'dolarow', '$', 'баксов', 'бакс',
                'долларов', 'доллар', 'доллара', 'дол', 'долл', ',frc', ',frcs', ',frcjd'],
        'EUR': ['EUR', 'euro', 'eur', 'euro', 'euro', 'euro', 'euro', '€', 'евро', 'евр',
                'эвро', 'эвр', 'еуро', 'еур', 'tdhj', 'tdh'],
        'PLN': ['PLN', 'zloty', 'pln', 'zloty', 'zlotego', 'zlotych', 'zlotow', 'zł', 'zl', 'zlot', 'zloty'
                'злотых', 'злот', 'зл', 'зло', 'злут', 'пол', 'пл', 'pl', 'pol', 'pkjn', 'pkjns['],
        'UAH': ['UAH', 'grivna', 'uah', 'grivna', 'grivny', 'griven', 'griven', '₴',
                'гривен', 'грив', 'грв', 'гр', 'uhbdys', 'uhd', 'uhbd'],
        'BYN': ['BYN', 'byn', 'rubl', 'rub', 'rubl', 'rublya', 'rubley', 'rubley', '₽', ',tkjr', ',kh', 'he,',
                'рублей', 'белорусски', 'белок', 'рубл', 'бел', 'беларус', 'блр', 'рбл']
    }

    __amount_separator = ['.']

    def __init__(self, text):
        # create class and set all attributes
        self.text = text
        # when create a class, parse currency and amount
        self.currency = self.parse_currency()
        self.amount = self.parse_amount()

    def parse_currency(self):
        # remove all numbers from text
        text = self.text.translate(str.maketrans('', '', string.digits))
        # search for keywords in text
        for currency in self.__keywords:
            for keyword in self.__keywords[currency]:
                # if keyword in text, set currency and return it
                if keyword in text:
                    self.currency = currency
                    return currency
        # if no keywords found, return None
        return None

    def parse_amount(self):
        # remove all letters from text
        text = self.text.translate(str.maketrans('', '', string.ascii_letters))
        # remove all whitespace from text
        text = text.translate(str.maketrans('', '', string.whitespace))
        # hold only numbers and delimeters
        for char in text:
            if not char.isdigit() and char not in self.__amount_separator:
                text = text.replace(char, '')
        try:
            self.amount = float(text)
            return float(text)
        except ValueError:
            # if have error to convert text to float, return None
            return None

    def __str__(self):
        # return string representation of class when print it
        return str(f"{self.amount} {self.currency}")
