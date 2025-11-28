import re
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Фильтрует транзакции по наличию строки search в поле description.

    :param data: Список словарей с транзакциями
    :param search: Строка для поиска в описании
    :return: Список словарей, где описание содержит search
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [transaction for transaction in data
            if
            "description" in transaction and transaction["description"] and pattern.search(transaction["description"])]


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчет количества транзакций по категориям из списка categories

    :param data: Список словарей с транзакциями
    :param categories: Список категорий для подсчета
    :return: Словарь {категория: количество}
    """
    counts: Dict[str, int] = {category: 0 for category in categories}
    for transaction in data:
        description = transaction.get("description", "")
        for category in categories:
            if description == category:
                counts[category] += 1
    return counts
