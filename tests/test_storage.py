import unittest
from unittest.mock import Mock, patch

from Kursownia.rates.local_storage import Storage


class TestStorage(unittest.TestCase):
    # skip this test
    @unittest.skip

    def setUp(self) -> None:
        self.storage = Storage()

    def test_init(self):
        self.assertEqual(self.storage.currencies, ['EUR', 'USD', 'PLN', 'BYN'])
        self.assertEqual(self.storage.updated_currencies, ['PLN', 'BYN', 'EUR'])

    @patch('Kursownia.rates.local_storage.rate_getter')
    def test_update_rates(self, mock_rate_getter):
        mock_rate_getter.request_pln_euro_rate.return_value = {'sell': 4.5, 'buy': 4.4}
        mock_rate_getter.request_pln_dollar_rate.return_value = {'sell': 3.5, 'buy': 3.4}
        mock_rate_getter.request_byn_rates.return_value = {'USD': {'buy': 2.5, 'sell': 2.4},
                                                           'EUR': {'buy': 3.5, 'sell': 3.4}}
        mock_rate_getter.get_crosshatches.return_value = {'USD': 0.5, 'EUR': 0.4}
        self.storage.update_rates()
        self.assertEqual(self.storage.PLN.get_rate('EUR'), 1 / 4.5)
        self.assertEqual(self.storage.PLN.get_rate('USD'), 1 / 3.5)
        self.assertEqual(self.storage.EUR.get_rate('PLN'), 4.4)
        self.assertEqual(self.storage.USD.get_rate('PLN'), 3.4)
        self.assertEqual(self.storage.BYN.get_rate('EUR'), 1 / 3.5)
        self.assertEqual(self.storage.BYN.get_rate('USD'), 1 / 2.5)
        self.assertEqual(self.storage.EUR.get_rate('USD'), 0.5)
        self.assertEqual(self.storage.USD.get_rate('EUR'), 1 / 0.4)


    def test_calculate(self):
        self.storage.calculate('EUR', 'USD', 1)
        self.storage.EUR.calc_rate.assert_called_with('USD', 1)
        self.storage.calculate('USD', 'EUR', 1)
        self.storage.USD.calc_rate.assert_called_with('EUR', 1)
        self.storage.calculate('PLN', 'EUR', 1)
        self.storage.PLN.calc_rate.assert_called_with('EUR', 1)
        self.storage.calculate('EUR', 'PLN', 1)
        self.storage.EUR.calc_rate.assert_called_with('PLN', 1)
        self.storage.calculate('PLN', 'USD', 1)
        self.storage.PLN.calc_rate.assert_called_with('USD', 1)
        self.storage.calculate('USD', 'PLN', 1)
        self.storage.USD.calc_rate.assert_called_with('PLN', 1)
        self.storage.calculate('PLN', 'BYN', 1)
        self.storage.PLN.calc_rate.assert_called_with('BYN', 1)
        self.storage.calculate('BYN', 'PLN', 1)
        self.storage.BYN.calc_rate.assert_called_with('PLN', 1)
        self.storage.calculate('EUR', 'BYN', 1)
        self.storage.EUR.calc_rate.assert_called_with('BYN', 1)
        self.storage.calculate('BYN', 'EUR', 1)
        self.storage.BYN.calc_rate.assert_called_with('EUR', 1)
        self.storage.calculate('USD', 'BYN', 1)


if __name__ == '__main__':
    unittest.main()
