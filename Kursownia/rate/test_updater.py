import unittest
from unittest.mock import patch, Mock
from updater import request_from_bank, find_euro, get_euro_rate

class TestBankExchangeRate(unittest.TestCase):

    @patch('updater.requests.get')
    def test_request_from_bank_successful(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [{"rates": [{"currency": "euro", "code": "EUR", "bid": 4.2, "ask": 4.3}]}]
        mock_get.return_value = mock_response

        result = request_from_bank()

        self.assertEqual(result["rates"][0]["code"], "EUR")
        self.assertEqual(result["rates"][0]["bid"], 4.2)
        self.assertEqual(result["rates"][0]["ask"], 4.3)

    @patch('updater.requests.get')
    def test_request_from_bank_error(self, mock_get):
        mock_get.side_effect = Exception("Test Exception")

        result = request_from_bank()

        self.assertFalse(result)

    def test_find_euro_found(self):
        test_data = {
            "rates": [
                {"currency": "US Dollar", "code": "USD", "bid": 4.0873, "ask": 4.1699},
                {"currency": "Euro", "code": "EUR", "bid": 4.2, "ask": 4.3}
            ]
        }

        result = find_euro(test_data)

        self.assertEqual(result["cur"], "EUR")
        self.assertEqual(result["buy"], 4.2)
        self.assertEqual(result["sold"], 4.3)

    def test_find_euro_not_found(self):
        test_data = {
            "rates": [
                {"currency": "US Dollar", "code": "USD", "bid": 4.0873, "ask": 4.1699},
                {"currency": "British Pound", "code": "GBP", "bid": 5.0, "ask": 5.1}
            ]
        }

        result = find_euro(test_data)

        self.assertEqual(result["cur"], "EUR")
        self.assertEqual(result["buy"], 0)
        self.assertEqual(result["sold"], 0)

    @patch('updater.request_from_bank')
    @patch('updater.find_euro')
    def test_get_euro_rate_successful(self, mock_find_euro, mock_request_from_bank):
        mock_request_from_bank.return_value = {"rates": [{"currency": "Euro", "code": "EUR", "bid": 4.2, "ask": 4.3}]}
        mock_find_euro.return_value = {"cur": "EUR", "buy": 4.2, "sold": 4.3}

        result = get_euro_rate()

        self.assertEqual(result["cur"], "EUR")
        self.assertEqual(result["buy"], 4.2)
        self.assertEqual(result["sold"], 4.3)

    @patch('updater.request_from_bank')
    def test_get_euro_rate_failed_api(self, mock_request_from_bank):
        mock_request_from_bank.return_value = False

        result = get_euro_rate()

        self.assertEqual(result, {"error": "Failed get from api"})

if __name__ == "__main__":
    unittest.main()
