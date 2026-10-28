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