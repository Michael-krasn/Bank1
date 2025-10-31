import sys
from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


def log(
        filename: Optional[str] = None)\
        -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Декоратор логирования выполнения функции.
    :param filename: путь к файлу для логов (если None — вывод в консоль)
    """

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message, file=sys.stderr)
                raise

        return wrapper

    return decorator
