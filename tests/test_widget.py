from typing import List, Tuple, Type

import pytest

from src.widget import mask_account_card

# ----------------------------
# ФИКСТУРЫ
# ----------------------------


@pytest.fixture
def valid_cases() -> List[Tuple[str, str]]:
    """Фикстура с корректными входными данными."""
    return [
        ("Счет 12345678901234567890", "Счет 7890"),
        ("Карта 1234567890123456", "Карта 1234 56** **** 3456"),
        ("Карта VISA 1234567890123456", "Карта VISA 1234 56** **** 3456"),
        ("Карта MasterCard 9876543210987654",
         "Карта MasterCard 9876 54** **** 7654"),
    ]


@pytest.fixture
def invalid_cases() -> List[Tuple[str, Type[Exception]]]:
    """Фикстура с некорректными входными данными."""
    return [
        ("", ValueError),  # пустая строка
        ("1234567890123456", ValueError),  # нет типа
        ("Счет", ValueError),  # нет номера
        ("Карта", ValueError),  # нет номера
        ("Счет 12345", ValueError),  # неверная длина счета
        ("Карта 12345", ValueError),  # неверная длина карты
        ("Счет 1234abcd901234567890", ValueError),  # буквы в номере счета
        ("Карта 1234abcd90123456", ValueError),  # буквы в номере карты
        ("Кошелек 1234567890123456", ValueError),  # неизвестный тип
    ]


# ----------------------------
# ПАРАМЕТРИЗИРОВАННЫЕ ТЕСТЫ
# ----------------------------

@pytest.mark.parametrize("data, expected", [
    ("Счет 12345678901234567890", "Счет 7890"),
    ("Карта 1234567890123456", "Карта 1234 56** **** 3456"),
    ("Карта VISA 1234567890123456", "Карта VISA 1234 56** **** 3456"),
])
def test_mask_account_card_valid_param(
    data: str,
    expected: str
) -> None:
    """Тест корректных данных с параметризацией."""
    assert mask_account_card(data) == expected


@pytest.mark.parametrize("data, exception", [
    ("", ValueError),
    ("1234567890123456", ValueError),
    ("Счет", ValueError),
    ("Карта", ValueError),
    ("Счет 12345", ValueError),
    ("Карта 12345", ValueError),
    ("Счет 1234abcd901234567890", ValueError),
    ("Карта 1234abcd90123456", ValueError),
    ("Кошелек 1234567890123456", ValueError),
])
def test_mask_account_card_invalid_param(
    data: str,
    exception: Type[Exception]
) -> None:
    """Тест некорректных данных с параметризацией."""
    with pytest.raises(exception):
        mask_account_card(data)


# ----------------------------
# ТЕСТЫ С ФИКСТУРАМИ
# ----------------------------

def test_mask_account_card_valid_with_fixture(
    valid_cases: List[Tuple[str, str]]
) -> None:
    """
    Тест с использованием фикстуры valid_cases для
    проверки корректной работы маскирования.

    Параметры:
    valid_cases (List[Tuple[str, str]]): список кортежей с тестовыми данными,
    где первый элемент - входные данные, второй - ожидаемый результат
    """
    for data, expected in valid_cases:
        assert mask_account_card(data) == expected


def test_mask_account_card_invalid_with_fixture(
        invalid_cases: List[Tuple[str, Type[Exception]]]
) -> None:
    """Тест с использованием фикстуры invalid_cases."""
    for data, exception in invalid_cases:
        # Убедимся, что exception является типом исключения
        assert isinstance(exception, type)
        assert issubclass(exception, Exception)

        with pytest.raises(exception):  # Теперь должно работать корректно
            mask_account_card(data)
