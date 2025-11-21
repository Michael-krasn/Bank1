import json
import os
from typing import Dict, List

from .logging_config import get_logger

logger = get_logger("utils")


def load_operations(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        logger.error("Файл не найден: %s", file_path)
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.error("Неверный формат данных в файле: %s", file_path)
            return []

        logger.info("Файл операций успешно загружен: %s", file_path)
        return data

    except json.JSONDecodeError:
        logger.exception("Ошибка JSON при чтении файла: %s", file_path)
        return []

    except IOError:
        logger.exception("Ошибка ввода-вывода при чтении файла: %s", file_path)
        return []
