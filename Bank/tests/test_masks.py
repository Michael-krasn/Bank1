import pytest

from src.masks import get_mask_account, get_mask_card_number

# ФИКСТУРЫ


@pytest.fixture
def valid_card_numbers() -> list[tuple[str, str]]:
    return [
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("9876543210987654", "9876 54** **** 7654"),
        (" 1234 5678 9012 3456 ", "1234 56** **** 3456"),
    ]


@pytest.fixture
def invalid_card_numbers() -> list[str]:
    return [
        "123456789012345",      # короткий
        "12345678901234567",    # длинный
        "",                     # пустой
        "1234abcd90123456",     # с буквами
        "1234!@#$90123456",     # с символами
    ]


@pytest.fixture
def valid_accounts() -> list[tuple[str, str]]:
    return [
        ("12049104570157075645", "**5645"),
        ("98765432109876543210", "**3210"),
    ]


@pytest.fixture
def invalid_accounts() -> list[str]:
    return [
        "1234567890123456789",      # короткий
        "123456789012345678901",    # длинный
        "",                         # пустой
        "1234abcd901234567890",     # буквы
        "1234!@#$901234567890",     # символы
        "1234 5678 9012 3456 7890",  # пробелы
    ]


# ТЕСТЫ ДЛЯ get_mask_card_number


@pytest.mark.parametrize("card, expected", [
    ("1234 5678 9012 3456", "1234 56** **** 3456"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("9876543210987654", "9876 54** **** 7654"),
    (" 1234 5678 9012 3456 ", "1234 56** **** 3456"),
])
def test_get_mask_card_number_valid(
        card: str,
        expected: str
) -> None:
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize("card", [
    "123456789012345",
    "12345678901234567",
    "",
    "1234abcd90123456",
    "1234!@#$90123456",
])
def test_get_mask_card_number_invalid(
        card: str
) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(card)


# ТЕСТЫ ДЛЯ get_mask_account


@pytest.mark.parametrize("account, expected", [
    ("12049104570157075645", "**5645"),
    ("98765432109876543210", "**3210"),
])
def test_get_mask_account_valid(
        account: str,
        expected: str
) -> None:
    assert get_mask_account(account) == expected


@pytest.mark.parametrize("account", [
    "1234567890123456789",
    "123456789012345678901",
    "",
    "1234abcd901234567890",
    "1234!@#$901234567890",
    "1234 5678 9012 3456 7890",
])
def test_get_mask_account_invalid(
        account: str
) -> None:
    with pytest.raises(ValueError):
        get_mask_account(account)
