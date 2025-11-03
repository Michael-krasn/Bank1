from typing import Any, Dict, Iterator, List


def filter_by_currency(
        transactions: List[Dict[str, Any]],
        currency: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, возвращающий транзакции, в которых код
    валюты совпадает с заданным.

    :param transactions: список словарей с транзакциями
    :param currency: строка с кодом валюты (например, 'USD')
    :return: итератор по отфильтрованным транзакциям
    """
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(
        transactions: List[Dict[str, Any]])\
        -> Iterator[str]:
    """
    Генератор, возвращающий описания транзакций.

    :param transactions: список словарей с транзакциями
    :return: итератор строк — описаний операций
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, создающий номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение диапазона (включительно)
    :param end: конечное значение диапазона (включительно)
    :return: итератор строк с номерами карт
    """
    if start < 1 or end > 9999_9999_9999_9999 or start > end:
        raise ValueError(
            "Диапазон должен быть от 1 до 9999 9999 9999 9999 и start <= end"
        )

    for num in range(start, end + 1):
        formatted = f"{num:016d}"
        yield " ".join(formatted[i:i + 4] for i in range(0, 16, 4))
