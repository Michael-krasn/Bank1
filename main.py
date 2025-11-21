from src.masks import get_mask_account, get_mask_card_number
from src.utils import load_operations

print("Начинаю работу main.py…")

# Вызов функций masks
try:
    masked_card = get_mask_card_number("1234 5678 9876 5432")
    print(masked_card)
except Exception as e:
    print("Ошибка:", e)

try:
    masked_account = get_mask_account("12345678901234567890")
    print(masked_account)
except Exception as e:
    print("Ошибка:", e)

# Вызов функции utils
load_operations("operations.json")  # файла может не быть, чтобы проверить лог ошибки

print("Работа main.py завершена.")