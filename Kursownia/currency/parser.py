import string


class TextToCurrencyParser:
    __keywords = {
        'USD': ['USD', 'dollar', 'dollars', 'usd', 'dolar', 'dolara', 'dolary', 'dolarow', '$', 'баксов', 'бакс', 'долларов', 'доллар',
                'доллара', 'дол', 'долл', 'до', 'бак', 'ба'],
        'EUR': ['EUR', 'euro', 'eur', 'euro', 'euro', 'euro', 'euro', '€', 'евро', 'евро', 'евро', 'евро', 'евро', 'евр',
                'эвро', 'эвр', 'ев', 'еуро', 'еур'],
        'PLN': ['PLN', 'zloty', 'pln', 'zloty', 'zlotego', 'zlotych', 'zlotow', 'zł', 'злотых', 'злотых', 'злотых', 'злотых',
                'злотых', 'злот', 'зл', 'зло', 'злут', 'пол', 'пл', 'pl', 'pol'],
        'UAH': ['UAH', 'grivna', 'uah', 'grivna', 'grivny', 'griven', 'griven', '₴', 'гривен', 'гривен', 'гривен', 'гривен',
                'гривен', 'грив', 'грв', 'гр'],
        'BYN': ['BYN', 'byn', 'rubl', 'rub', 'rubl', 'rublya', 'rubley', 'rubley', '₽', 'рублей', 'рублей', 'рублей', 'рублей',
                'рублей', 'белорусски', 'белок', 'рубл', 'бел', 'беларус', 'блр', 'рбл']
    }

    __amount_separator = ['.']

    def __init__(self, text):
        self.text = text
        self.currency = self.parse_currency()
        self.amount = self.parse_amount()

    def parse_currency(self):
        # remove all numbers from text
        text = self.text.translate(str.maketrans('', '', string.digits))
        for currency in self.__keywords:
            for keyword in self.__keywords[currency]:
                if keyword in text:
                    self.currency = currency
                    return currency
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
        self.amount = float(text)
        return float(text)

    def __str__(self):
        return str(f"{self.amount} {self.currency}")
