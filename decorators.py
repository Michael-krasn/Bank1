import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar, Optional

# Параметры типа для сохранения сигнатуры функции
P = ParamSpec("P")
R = TypeVar("R")

def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Декоратор для логирования вызовов функций.

    Параметры:
        filename: Путь к файлу лога. Если None — вывод в консоль.

    Возвращает:
        Декоратор, оборачивающий функцию с логированием.
    """
    def wrapper(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def inner(*args: P.args, **kwargs: P.kwargs) -> R:
            start_time = time.time()
            log_message = ""

            try:
                result = func(*args, **kwargs)
                exec_time = time.time() - start_time
                log_message = (
                    f"Функция: {func.__name__} "
                    f"Результат: {result} "
                    f"Время: {exec_time:.4f} сек"
                )
                return result

            except Exception as e:
                exec_time = time.time() - start_time
                log_message = (
                    f"Ошибка в функции: {func.__name__} "
                    f"Ошибка: {type(e).__name__}: {e} "
                    f"Аргументы: args={args}, kwargs={kwargs} "
                    f"Время: {exec_time:.4f} сек"
                )
                raise  # Пробрасываем исключение

            finally:
                # Запись лога (выполняется всегда, даже при исключении)
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

        return inner

    return wrapper



@log("mylog.txt")
def my_func_div(x: float, y: float) -> float:
    """
    Функция сложения двух чисел.

    Параметры:
        x: Первое число.
        y: Второе число.

    Возвращает:
        Сумма x и y.
    """
    return x + y



# Вызов функции
my_func_div(20.0, 0.0)
