import time
import functools
from typing import Callable, Any
from functools import reduce


def time_it(func: Callable) -> Callable:
    """Декоратор для замера времени выполнения функции."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[{func.__name__}] выполнена за {end_time - start_time:.4f} сек")
        return result
    return wrapper


def apply_multiple_funcs(funcs: list[Callable], data: list[Any]) -> list[list[Any]]:
    """Применяет несколько функций к списку через map."""
    return [list(map(f, data)) for f in funcs]


def factorial_reduce(n: int) -> int:
    """Вычисляет факториал числа с использованием reduce."""
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    if n == 0:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))