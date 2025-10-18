from datetime import datetime
from typing import Dict, List


def filter_by_state(banking_operation: List[Dict[str, str]], state="EXECUTED"):
    """функция принимает на вход списик словарей и параметр сортировки,
    возвращает новый отсортированный список по параметру. 'state'"""

    return [x for x in banking_operation if x["state"] == state]


def sort_by_date(
    banking_operation: List[Dict[str, str]], reverse: bool = True
) -> List[Dict[str, str]]:
    """Функция принимает на вход список словарей и параметр порядка
    сортировки, возвращает новый список, в котором исходные словари
    отсортированы по дате."""
    return sorted(
        banking_operation, key=lambda x: 
        datetime.fromisoformat(x["date"]), reverse=True
    )
