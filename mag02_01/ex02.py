from time import time, time_ns
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
    time_ns()
    start = time_ns()
    print(start)
    print(fibonacci_memo(150))
    end = time_ns()
    print(end)
    print(f"MEMO: {end - start}")
    time_ns()
    start = time()
    print(fibonacci(150))
    print(f"LRU: {time() - start}")
    time_ns()
    start = time()
    print(fibonacci_slow(15))
    print(f"NO MEMO: {time() - start}")
