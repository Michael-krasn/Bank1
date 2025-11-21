from .logging_config import get_logger

logger = get_logger("masks")


def get_mask_card_number(card_number: str) -> str:
    cleaning_number_card = card_number.replace(" ", "")

    if not cleaning_number_card.isdigit():
        logger.error("Номер карты содержит недопустимые символы: %s", card_number)
        raise ValueError("Номер карты должен состоять только из цифр")

    if len(cleaning_number_card) != 16:
        logger.error("Некорректная длина номера карты: %s", card_number)
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_part = cleaning_number_card[:6] + "*" * 6 + cleaning_number_card[-4:]
    formatted_mask = " ".join(
        [masked_part[i:i + 4] for i in range(0, len(masked_part), 4)]
    )

    logger.info("Номер карты успешно замаскирован: %s", formatted_mask)
    return formatted_mask


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, отображая только последние 4 цифры с маской '**' перед ними."""

    if not account_number:
        logger.error("Пустой номер счета")
        raise ValueError("Номер счета не может быть пустым")

    if not account_number.isdigit():
        logger.error("Номер счета содержит недопустимые символы: %s", account_number)
        raise ValueError("Номер счета может содержать только цифры")

    if len(account_number) != 20:
        logger.error("Некорректная длина номера счета: %s", account_number)
        raise ValueError("Номер счета должен содержать 20 цифр")

    masked_account = f"**{account_number[-4:]}"  # добавляем две звёздочки перед последними 4 цифрами
    logger.info("Номер счета успешно замаскирован: %s", masked_account)
    return masked_account
