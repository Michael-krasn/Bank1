import unittest
from src.widget import mask_account_card


class TestMaskingFunctions(unittest.TestCase):

    def test_invalid_input(self):
        # Отсутствует тип операции
        with self.assertRaises(ValueError):
            mask_account_card("1234567890123456")

        # Отсутствует номер счета
        with self.assertRaises(ValueError):
            mask_account_card("Счет")

        # Отсутствует номер карты
        with self.assertRaises(ValueError):
            mask_account_card("Карта")

        # Неизвестный тип операции
        with self.assertRaises(ValueError):
            mask_account_card("Кошелек 1234567890123456")

    def test_valid_cases(self):
        # Корректный номер счета
        self.assertEqual(
            mask_account_card("Счет 12345678901234567890"),
            "Счет **7890"
        )

        # Корректный номер карты
        self.assertEqual(
            mask_account_card("Карта 1234567890123456"),
            "Карта 1234 56** **** 3456"
        )


if __name__ == '__main__':
    unittest.main()