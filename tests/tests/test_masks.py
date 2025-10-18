import unittest
from typing import Self, Type

from parameterized import parameterized  # type: ignore

from src.masks import get_mask_account, get_mask_card_number


class TestMaskingFunctions(unittest.TestCase):

    # Валидные тесты для карт
    @parameterized.expand([
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        ("1234 56 7890 123456", "1234 56** **** 3456"),
        (" 1234 5678 9012 3456 ", "1234 56** **** 3456"),
        ("1234  5678    9012   3456", "1234 56** **** 3456")
    ])
    def test_card_number_valid(self, input_data, expected):
        self.assertEqual(get_mask_card_number(input_data), expected)

    # Невалидные тесты для карт
    @parameterized.expand([
        ("123456789012345", ValueError),  # короче 16 цифр
        ("12345678901234567", ValueError),  # длиннее 16 цифр
        ("", ValueError),  # пустая строка
        ("1234abcd90123456", ValueError),  # с буквами
        ("1234!@#$90123456", ValueError)  # со спецсимволами
    ])
    def test_card_number_invalid(
            self: Self,  # Явное указание типа для self
            input_data: str,  # Входной номер карты
            expected_exception: Type[Exception]  # Ожидаемое исключение
    ) -> None:  # Функция ничего не возвращает
        """
        Тестовый метод для проверки обработки некорректных номеров карт
        """
        with self.assertRaises(expected_exception):
            get_mask_card_number(input_data)

    # Валидные тесты для счетов
    @parameterized.expand([
        ("12049104570157075645", "**5645"),
        ("98765432109876543210", "**3210")
    ])
    def test_account_number_valid(
        self: Self,  # Явное указание типа для self
        input_data: str,  # Входной номер счета
        expected: str  # Ожидаемый результат маскирования
    ) -> None:  # Функция ничего не возвращает
        """
        Тестовый метод для проверки корректной работы маскирования номера счета
        """
        self.assertEqual(get_mask_account(input_data), expected)

    # Невалидные тесты для счетов
    @parameterized.expand([
        ("1234567890123456789", ValueError),  # короче 20 цифр
        ("123456789012345678901", ValueError),  # длиннее 20 цифр
        ("", ValueError),  # пустая строка
        ("1234abcd901234567890", ValueError),  # с буквами
        ("1234!@#$901234567890", ValueError),  # со спецсимволами
        ("1234 5678 9012 3456 7890", ValueError)  # с пробелами
    ])
    def test_account_number_invalid(
        self: Self,   # Ссылка на текущий экземпляр класса
        input_data: str,   # Некорректный номер счета для тестирования
        expected_exception: Type[Exception]
    ) -> None:                       # Метод не возвращает значение
        """
        Тестовый метод для проверки обработки некорректных номеров счетов
        """
        with self.assertRaises(expected_exception):
            get_mask_account(input_data)


if __name__ == '__main__':
    unittest.main()
