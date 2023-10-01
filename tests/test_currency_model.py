import unittest

from Kursownia.currency.models import Currency


class TestCurrency(unittest.TestCase):

    def test_init(self):
        currency = Currency("USD")
        self.assertEqual(currency.code, "USD")

    def test_str(self):
        currency = Currency("EUR")
        self.assertEqual(str(currency), "EUR")

    def test_set_rate(self):
        currency = Currency("USD")
        currency.set_rate("EUR", 1.10)
        self.assertEqual(currency.EUR, 1.10)

    def test_set_rate_negative(self):
        currency = Currency("USD")
        with self.assertRaises(ValueError):
            currency.set_rate("EUR", -1.10)

    def test_set_rate_zero(self):
        currency = Currency("USD")
        with self.assertRaises(ValueError):
            currency.set_rate("EUR", 0)

    def test_get_rate(self):
        currency = Currency("USD")
        currency.set_rate("EUR", 1.10)
        self.assertEqual(currency.get_rate("EUR"), 1.10)

    def test_calc_rate(self):
        currency = Currency("USD")
        currency.set_rate("EUR", 1.10)
        self.assertEqual(currency.calc_rate("EUR", 100), 110.00)


if __name__ == '__main__':
    unittest.main()
