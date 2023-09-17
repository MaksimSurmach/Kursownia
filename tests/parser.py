import unittest

from Kursownia.currency.parser import TextToCurrencyParser


class MyTestCase(unittest.TestCase):
    def test_parse_text_to_currency(self):
        text1 = "I have 100 dollars"
        parser1 = TextToCurrencyParser(text1)
        self.assertEqual(parser1.currency, 'USD')
        self.assertEqual(parser1.amount, 100)

        text2 = "20€ for a book"
        parser2 = TextToCurrencyParser(text2)
        self.assertEqual(parser2.currency, 'EUR')
        self.assertEqual(parser2.amount, 20)

        text3 = "500 гривен"
        parser3 = TextToCurrencyParser(text3)
        self.assertEqual(parser3.currency, 'UAH')
        self.assertEqual(parser3.amount, 500)

        text4 = "50 рублей"
        parser4 = TextToCurrencyParser(text4)
        self.assertEqual(parser4.currency, 'BYN')
        self.assertEqual(parser4.amount, 50)

        text5 = "This is a test"
        parser5 = TextToCurrencyParser(text5)
        self.assertIsNone(parser5.currency)
        self.assertIsNone(parser5.amount)

    def test_parse_currency(self):
        text1 = "I have 100 dollars"
        parser1 = TextToCurrencyParser(text1)
        self.assertEqual(parser1.currency, 'USD')

        text2 = "20€ for a book"
        parser2 = TextToCurrencyParser(text2)
        self.assertEqual(parser2.currency, 'EUR')

        text3 = "500 гривен"
        parser3 = TextToCurrencyParser(text3)
        self.assertEqual(parser3.currency, 'UAH')

        text4 = "50 рублей"
        parser4 = TextToCurrencyParser(text4)
        self.assertEqual(parser4.currency, 'BYN')

        text5 = "This is a test"
        parser5 = TextToCurrencyParser(text5)
        self.assertIsNone(parser5.currency)

        text6 = "100₹ for dinner"
        parser6 = TextToCurrencyParser(text6)
        self.assertIsNone(parser6.currency)

        text7 = "15.5 pln for a ticket"
        parser7 = TextToCurrencyParser(text7)
        self.assertEqual(parser7.currency, 'PLN')

        text8 = "10.75 dollars for coffee"
        parser8 = TextToCurrencyParser(text8)
        self.assertEqual(parser8.currency, 'USD')

        text9 = "30.25 € for a movie"
        parser9 = TextToCurrencyParser(text9)
        self.assertEqual(parser9.currency, 'EUR')

        text10 = "50.75 гривен"
        parser10 = TextToCurrencyParser(text10)
        self.assertEqual(parser10.currency, 'UAH')

        text11 = "99.99 rubles for a book"
        parser11 = TextToCurrencyParser(text11)
        self.assertEqual(parser11.currency, 'BYN')

        text12 = "10 yuan for lunch"
        parser12 = TextToCurrencyParser(text12)
        self.assertIsNone(parser12.currency)

    def test_parse_amount(self):
        text1 = "I have 100 dollars"
        parser1 = TextToCurrencyParser(text1)
        self.assertEqual(parser1.amount, 100)
        self.assertEqual(parser1.currency, 'USD')

        text2 = "20€ for a book"
        parser2 = TextToCurrencyParser(text2)
        self.assertEqual(parser2.amount, 20)
        self.assertEqual(parser2.currency, 'EUR')

        text3 = "500 гривен"
        parser3 = TextToCurrencyParser(text3)
        self.assertEqual(parser3.amount, 500)
        self.assertEqual(parser3.currency, 'UAH')

        text4 = "50 рублей"
        parser4 = TextToCurrencyParser(text4)
        self.assertEqual(parser4.amount, 50)
        self.assertEqual(parser4.currency, 'BYN')

        text5 = "No amount mentioned"
        parser5 = TextToCurrencyParser(text5)
        self.assertIsNone(parser5.amount)
        self.assertIsNone(parser5.currency)

        text6 = "I have $5.75"
        parser6 = TextToCurrencyParser(text6)
        self.assertEqual(parser6.amount, 5)
        self.assertEqual(parser6.currency, 'USD')

        text7 = "20.5€ for a movie ticket"
        parser7 = TextToCurrencyParser(text7)
        self.assertEqual(parser7.amount, 20)
        self.assertEqual(parser7.currency, 'EUR')

        text8 = "10.75 гривен"
        parser8 = TextToCurrencyParser(text8)
        self.assertEqual(parser8.amount, 10)
        self.assertEqual(parser8.currency, 'UAH')

        text9 = "15.99 rubles"
        parser9 = TextToCurrencyParser(text9)
        self.assertEqual(parser9.amount, 15)
        self.assertEqual(parser9.currency, 'BYN')

        text10 = "I have 10.5 EUR"
        parser10 = TextToCurrencyParser(text10)
        self.assertEqual(parser10.amount, 10)
        self.assertEqual(parser10.currency, 'EUR')

        text11 = "50.75 yuan"
        parser11 = TextToCurrencyParser(text11)
        self.assertEqual(parser11.amount, 50)
        self.assertIsNone(parser11.currency)

        text12 = "No amount mentioned"
        parser12 = TextToCurrencyParser(text12)
        self.assertIsNone(parser12.amount)
        self.assertIsNone(parser12.currency)

    def test_invalid_currency(self):
        text1 = "I have 100 yen"
        parser1 = TextToCurrencyParser(text1)
        self.assertIsNone(parser1.currency)
        self.assertEqual(parser1.amount, 100)

        text2 = "20 CAD for a book"
        parser2 = TextToCurrencyParser(text2)
        self.assertIsNone(parser2.currency)
        self.assertEqual(parser2.amount, 20)

        text3 = "500 GBP"
        parser3 = TextToCurrencyParser(text3)
        self.assertIsNone(parser3.currency)
        self.assertEqual(parser3.amount, 500)

        text4 = "50 CHF"
        parser4 = TextToCurrencyParser(text4)
        self.assertIsNone(parser4.currency)
        self.assertEqual(parser4.amount, 50)

if __name__ == '__main__':
    unittest.main()
