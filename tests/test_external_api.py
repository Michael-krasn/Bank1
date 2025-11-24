import unittest
from unittest.mock import Mock, patch

import requests

from src.external_api import get_rub_amount


class TestGetRubAmount(unittest.TestCase):

    def test_rub_no_conversion(self) -> None:
        transaction = {
            'operationAmount': {
                'amount': '5000.00',
                'currency': {'code': 'RUB'}
            }
        }
        result = get_rub_amount(transaction)
        self.assertEqual(result, 5000.0)

    @patch('src.external_api.os.getenv', return_value='test_key')
    @patch('src.external_api.requests.get')
    def test_usd_to_rub(self, mock_get: Mock, mock_getenv: Mock) -> None:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {'RUB': '75.0'}
        }
        mock_get.return_value = mock_response

        transaction = {
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'USD'}
            }
        }

        result = get_rub_amount(transaction)
        self.assertAlmostEqual(result, 7500.0)

    @patch('src.external_api.os.getenv', return_value='test_key')
    @patch('src.external_api.requests.get', side_effect=requests.exceptions.RequestException)
    def test_api_request_failure(self, mock_get: Mock, mock_getenv: Mock) -> None:
        transaction = {
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'EUR'}
            }
        }
        result = get_rub_amount(transaction)
        self.assertEqual(result, 0.0)

    @patch('src.external_api.os.getenv', return_value=None)
    def test_missing_api_key(self, mock_getenv: Mock) -> None:
        transaction = {
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'USD'}
            }
        }
        result = get_rub_amount(transaction)
        self.assertEqual(result, 0.0)


if __name__ == '__main__':
    unittest.main()