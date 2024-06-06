"""Project Euler Problem 2: Even Fibonacci numbers."""
from functools import cache
import numpy as np

@cache
def fib_recursive(n: int) -> int:
    """Return the nth Fibonacci number by recursion."""
    if n <= 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_closed(n: int) -> int:
    """Return the nth Fibonacci number by Binet's formula."""
    φ = (1 + 5 ** 0.5) / 2
    ψ = (1 - 5 ** 0.5) / 2
    return int((φ ** (n + 1) - ψ ** (n + 1)) / (φ - ψ))

def fib_iterative(n: int) -> int:
    """Return the nth Fibonacci number by iteration."""
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_list(n : int) -> int:
    """Return the n Fibonacci numbers in a list."""
    if n == 0:
        return []
    elif n == 1:
        return [1]
    fibs = [1, 1]
    for _ in range(n - 2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def fib_list_max(maxsize: int = 0) -> list[int]:
    """Return the Fibonacci numbers that do not exceed maxsize in a list."""
    if maxsize == 0:
        return []
    fibs = [1, 1]
    while fibs[-1] <= maxsize:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[:-1]

def fib_list_even_max(maxsize: int = 0) -> list[int]:
    """Return the even Fibonacci numbers that do not exceed maxsize in a list."""
    if maxsize in {0, 1}:
        return []
    fibs = [2, 8]
    while fibs[-1] <= maxsize:
        fibs.append(4 * fibs[-1] + fibs[-2])
    return fibs[:-1]

def solution(maxsize: int = 0) -> int:
    """Return the sum of the even Fibonacci numbers, up to maxsize."""
    return sum(fib_list_even_max(maxsize))

if __name__ == "__main__":
    print(solution(4_000_000))
