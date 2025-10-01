def mask_account_card(data: str) -> str:
    """
    Функция для маскировки номера карты или счета.
    """
    # Разделяем строку на тип и номер
    parts = data.split()

    # Если это счет
    if parts[0] == "Счет":
        account_number = parts[-1]
        # Маскируем последние 4 цифры
        masked_acc = f"**{account_number[-4:]}"
        return f"{parts[0]} {masked_acc}"

    # Если это карта
    else:
        card_number = parts[-1]
        card_name = " ".join(parts[:-1])
        # Маскируем номер карты
        masked_card = (
            f"{card_number[:4]} "
            f"{card_number[4:6]}** "
            f"**** "
            f"{card_number[-4:]}"
        )
        return f"{card_name} {masked_card}"
