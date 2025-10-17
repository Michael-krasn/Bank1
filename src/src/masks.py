def get_mask_card_number(card_number: str) -> str:
    """Маскируем данные карты по формату -
    первые 6 и последние 4 цифры видны, остальные закрыты. ****
    Формат: XXXX XX** **** XXXX"""

    # Удаляем все пробелы из входных данных
    cleaning_number_card = card_number.replace(" ", "")

    # Проверяем строку на содержание букв
    if not cleaning_number_card.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр")

    # Проверяем длину заполненных данных на соответствие
    # количеству цифр в номере карты
    if len(cleaning_number_card) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

        # Создаем маску
    masked_part = (cleaning_number_card[:6] +
                   "**" + "*" * 4 + cleaning_number_card[-4:])

    # Форматируем в группы по 4 символа с пробелами
    formatted_mask = " ".join(
        [masked_part[i:i + 4] for i in range(0, len(masked_part), 4)]
    )

    return formatted_mask


def get_mask_account(account_number: str) -> str:
    """ " Маскирует номер счета, отображая только последние 4 цифры.
    Формат: Ввод: 12049104570157075645
            Вывод: **7075"""

    # Проверяем заполненность поля.
    if not account_number:
        raise ValueError("Номер счета не может быть пустым")

    # Проверяем на наличие символов кроме цифр.
    if not account_number.isdigit():
        raise ValueError("Номер счета может содержать только цифры")

    # Проверяем длину заполненных данных на соответствие
    # количеству цифр в номере карты.
    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")

    masked_account = f"**{account_number[-4:]}"

    return masked_account
