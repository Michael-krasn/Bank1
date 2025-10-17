import unittest

from parameterized import parameterized  # type: ignore

from src.widget import mask_account_card


class TestMaskingFunctions(unittest.TestCase):

    # Параметризованный тест для невалидных входных данных
    @parameterized.expand([
        ("1234567890123456", ValueError),  # Отсутствует тип операции
        ("Счет", ValueError),  # Отсутствует номер счета
        ("Карта", ValueError),  # Отсутствует номер карты
        ("Кошелек 1234567890123456", ValueError)  # Неизвестный тип операции
    ])
    def test_invalid_input(self, input_data, expected_exception):
        with self.assertRaises(expected_exception):
            mask_account_card(input_data)

    # Параметризованный тест для валидных случаев
    @parameterized.expand([
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Карта 1234567890123456", "Карта 1234 56** **** 3456")
    ])
    def test_valid_cases(self, input_data, expected_output):
        self.assertEqual(mask_account_card(input_data), expected_output)


if __name__ == '__main__':
    unittest.main()
