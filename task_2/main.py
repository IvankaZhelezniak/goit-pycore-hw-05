from typing import Callable, Iterable
import re


text = "Загальний дохід працівника складається з декількох частин: /" \
"1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Функція-генератор для знаходження дійсних чисел у тексті
def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'              # регулярний вираз для дійсних чисел
    matches = re.findall(pattern, text)    # пошук всіх збігів
    for match in matches:
        yield float(match)                 # yield — повертає по одному числу

# Функція для обчислення загальної суми чисел (прибутку)
def sum_profit(text: str, func: Callable[[str], Iterable[float]]) -> float:
    return sum(func(text))                 # підсумовує всі значення з генератора

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")