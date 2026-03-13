def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
# Эта строка специально сделана невероятно длинной, чтобы инструмент проверки стиля flake8 выдал нам ошибку нарушения стандарта PEP8, потому что строки не должны быть длиннее 88 символов.
