import os
from decimal import Decimal, InvalidOperation
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def get_rub_amount(transaction: Dict) -> float:
    """
    Возвращает сумму транзакции в рублях.

    Args:
        transaction: словарь с данными транзакции

    Returns:
        Сумма в рублях (float)
    """
    try:
        amount = Decimal(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']

        # Если валюта уже RUB - просто возвращаем сумму
        if currency == 'RUB':
            return float(amount)

        # Получаем API-ключ и URL из переменных окружения
        api_key = os.getenv('API_KEY')
        api_url = os.getenv('API_URL')

        # Если нет API-ключа или URL - возвращаем 0
        if not api_key or not api_url:
            return 0.0

        # Делаем запрос к API для получения курсов
        response = requests.get(
            api_url,
            params={
                'access_key': api_key,
                'base': currency,
                'symbols': 'RUB'
            },
            timeout=10
        )
        response.raise_for_status()  # Поднимает исключение при HTTP-ошибке

        data = response.json()
        rate = Decimal(data['rates']['RUB'])
        rub_amount = amount * rate

        return float(rub_amount)

    except (
            requests.RequestException,
            KeyError,
            InvalidOperation,
            ValueError
    ):
        return 0.0
