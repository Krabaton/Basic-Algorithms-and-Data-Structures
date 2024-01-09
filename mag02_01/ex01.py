def factorial(n):
    if n == 0:  # базовий випадок
        return 1
    else:
        return n * factorial(n - 1)  # рекурсивний випадок


print(factorial(5))  # виведе 120
