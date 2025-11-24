import unittest
from unittest.mock import Mock, mock_open, patch

from src.utils import load_operations


class TestLoadOperations(unittest.TestCase):

    @patch('os.path.exists', return_value=False)
    def test_file_not_found(self, mock_exists: Mock) -> None:
        result = load_operations('non_existent.json')
        self.assertEqual(result, [])

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='{"not": "a list"}')
    def test_not_a_list(self, mock_file: Mock, mock_exists: Mock) -> None:
        result = load_operations('invalid.json')
        self.assertEqual(result, [])

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1}]')
    def test_valid_json_list(self, mock_file: Mock, mock_exists: Mock) -> None:
        result = load_operations('valid.json')
        self.assertEqual(result, [{"id": 1}])

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', side_effect=IOError)
    def test_io_error(self, mock_file: Mock, mock_exists: Mock) -> None:
        result = load_operations('error.json')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()