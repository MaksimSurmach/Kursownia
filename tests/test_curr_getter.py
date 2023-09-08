import unittest
import requests
from Kursownia.rates.rate_getter import request_euro_rate, request_dollar_rate

class TestCurrencyRatesEUR(unittest.TestCase):

    def test_request_euro_rate(self):
        euro_rate = request_euro_rate()
        self.assertIsNotNone(euro_rate)
        self.assertIsInstance(euro_rate, (int, float))
        self.assertGreater(euro_rate, 0)

class TestCurrencyRatesDollar(unittest.TestCase):
    def test_request_dollar_rate(self):
        dollar_rate = request_dollar_rate()
        self.assertIsNotNone(dollar_rate)
        self.assertIsInstance(dollar_rate, (int, float))
        self.assertGreater(dollar_rate, 0)

