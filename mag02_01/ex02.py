from time import time, time_ns, ctime
import timeit
from functools import lru_cache


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    else:
        value = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        memo[n] = value
        return value


@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        return value


def fibonacci_slow(n):
    if n <= 1:
        return n
    else:
        value = fibonacci_slow(n - 1) + fibonacci_slow(n - 2)
        return value


if __name__ == "__main__":
    start = time_ns()
    f = fibonacci_memo(400)
    print(f"MEMO: {time_ns() - start}")

    start = time_ns()
    f = fibonacci(400)
    print(f"LRU: {time_ns() - start}")

    start = time_ns()
    f = fibonacci_slow(15)
    print(f"NO MEMO: {time_ns() - start}")

    # Вимірювання часу за допомогою timeit

    n = 15  # для fibonacci_memo і fibonacci
    n_slow = 15  # для fibonacci_slow

    time_memo = timeit.timeit("fibonacci_memo(n)", globals=globals(), number=10)
    time_lru = timeit.timeit("fibonacci(n)", globals=globals(), number=10)
    time_slow = timeit.timeit("fibonacci_slow(n_slow)", globals=globals(), number=10)

    print(f"Час виконання fibonacci_memo: {time_memo} секунд")
    print(f"Час виконання fibonacci (LRU): {time_lru} секунд")
    print(f"Час виконання fibonacci_slow: {time_slow} секунд")
