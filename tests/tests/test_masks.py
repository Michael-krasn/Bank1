import unittest
from src.masks import get_mask_card_number, get_mask_account


class TestMaskingFunctions(unittest.TestCase):

    # Тесты для функции get_mask_card_number
    def test_card_number_valid(self):
        # Базовый тест с корректным номером карты
        self.assertEqual(
            get_mask_card_number("1234 5678 9012 3456"),
            "1234 56** **** 3456"
        )

        # Тест с номером без пробелов
        self.assertEqual(
            get_mask_card_number("1234567890123456"),
            "1234 56** **** 3456"
        )

        # Тест с номером, содержащим только цифры
        self.assertEqual(
            get_mask_card_number("9876543210987654"),
            "9876 54** **** 7654"
        )

    def test_card_number_invalid_length(self):
        # Номер короче 16 цифр
        with self.assertRaises(ValueError):
            get_mask_card_number("123456789012345")

        # Номер длиннее 16 цифр
        with self.assertRaises(ValueError):
            get_mask_card_number("12345678901234567")

        # Пустая строка
        with self.assertRaises(ValueError):
            get_mask_card_number("")

    def test_card_number_invalid_characters(self):
        # Строка с буквами
        with self.assertRaises(ValueError):
            get_mask_card_number("1234abcd90123456")

        # Строка со специальными символами
        with self.assertRaises(ValueError):
            get_mask_card_number("1234!@#$90123456")

        # Проверка корректной работы с разными пробелами
        self.assertEqual(
            get_mask_card_number("1234 56 7890 123456"),
            "1234 56** **** 3456"
        )

        # Проверка с лишними пробелами
        self.assertEqual(
            get_mask_card_number(" 1234 5678 9012 3456 "),
            "1234 56** **** 3456"
        )

        # Проверка с множественными пробелами
        self.assertEqual(
            get_mask_card_number("1234  5678    9012   3456"),
            "1234 56** **** 3456"
        )

    # Тесты для функции get_mask_account
    def test_account_number_valid(self):
        # Базовый тест с корректным номером счета
        self.assertEqual(
            get_mask_account("12049104570157075645"),
            "**5645"
        )

        # Тест с другим корректным номером
        self.assertEqual(
            get_mask_account("98765432109876543210"),
            "**3210"
        )

    def test_account_number_invalid_length(self):
        # Номер короче 20 цифр
        with self.assertRaises(ValueError):
            get_mask_account("1234567890123456789")

        # Номер длиннее 20 цифр
        with self.assertRaises(ValueError):
            get_mask_account("123456789012345678901")

        # Пустая строка
        with self.assertRaises(ValueError):
            get_mask_account("")

    def test_account_number_invalid_characters(self):
        # Строка с буквами
        with self.assertRaises(ValueError):
            get_mask_account("1234abcd901234567890")

        # Строка со специальными символами
        with self.assertRaises(ValueError):
            get_mask_account("1234!@#$901234567890")

        # Строка с пробелами
        with self.assertRaises(ValueError):
            get_mask_account("1234 5678 9012 3456 7890")


if __name__ == '__main__':
    unittest.main()
