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


def process_csv(file_path: str) -> list[dict[str, Any]]:
    """Читает CSV, фильтрует (age >= 25) и преобразует данные через map и filter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    if len(lines) <= 1:
        return []
        
    headers = lines[0].strip().split(',')
    
    # map: превращаем строки в словари
    data_dicts = map(lambda line: dict(zip(headers, line.strip().split(','))), lines[1:])
    
    # filter: оставляем только тех, кому 25 и больше лет
    filtered_data = filter(lambda d: int(d.get('age', 0)) >= 25, data_dicts)
    
    # map: увеличиваем зарплату на 10%
    def transform(d: dict[str, Any]) -> dict[str, Any]:
        d['salary'] = round(float(d['salary']) * 1.1, 2)
        return d
        
    return list(map(transform, filtered_data))