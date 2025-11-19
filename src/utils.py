import json
import os
from typing import Dict, List


def load_operations(file_path: str) -> List[Dict]:
    """
    Загружает список операций из JSON-файла.

    Args:
        file_path: путь к JSON-файлу

    Returns:
        Список словарей с данными операций или пустой список в случае ошибок
    """
    # Проверяем существование файла
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Проверяем, что данные - список
        if not isinstance(data, list):
            return []

        return data

    except (json.JSONDecodeError, IOError):
        return []
