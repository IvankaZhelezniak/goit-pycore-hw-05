# Завдання: Створити функцію, яка обчислює числа Фібоначчі з використанням кешування.

def caching_fibonacci():
    cache_dict = {}            # Словник для зберігання кешованих значень

    def fibonacci(n):  
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache_dict:                             # Перевіряємо, чи є значення в кеші
            return cache_dict[n]
        
        cache_dict[n] = fibonacci(n-1) + fibonacci(n-2)  # Обчислюємо значення та зберігаємо в кеш
        return cache_dict[n]                             # Повертаємо обчислене значення
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610