def mask_account_card(data: str) -> str:
    parts = data.split()

    if not parts:
        raise ValueError("Неверный формат данных")

    if parts[0] == "Счет":
        account_number = parts[-1]

        if not account_number.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")

        if len(account_number) != 20:
            raise ValueError("Номер счета должен содержать 20 цифр")

        masked_acc = f"{account_number[-4:]}"
        return f"{parts[0]} {masked_acc}"

    elif parts[0] == "Карта":
        card_number = parts[-1]
        card_name = " ".join(parts[:-1])

        if not card_number.isdigit():
            raise ValueError("Номер карты должен содержать только цифры")

        if len(card_number) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")

        masked_card = (
            f"{card_number[:4]} "
            f"{card_number[4:6]}** "
            f"**** "
            f"{card_number[-4:]}"
        )
        return f"{card_name} {masked_card}"

    else:
        raise ValueError("Неверный формат данных")
