from collections.abc import Iterable

def solution_brute(n: int = 1000) -> int:
    for a in range(1, n):
        for b in range(a, n):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

# part 5
def prod(iterable: Iterable[int], /, *, start: int = 1) -> int:
    """Returns the product of all elements in an iterable."""
    result = start
    for i in iterable:
        result *= i
    return result

def find_triplet(sum_: int) -> int:
    # source: https://projecteuler.net/thread=9#628
    # returns a, b, c
    m = 0
    for n in range(sum_ + 1):
        delta = n**2 + 2 * sum_
        m1 = (-n + delta**0.5) / 2
        m2 = (-n - delta**0.5) / 2
        if m1.is_integer() and m1 > n:
            m = int(m1)
        elif m2.is_integer() and m2 > n:
            m = int(m2)
        if m:
            return 2*m*n, m**2 - n**2, m**2 + n**2
        
def solution(n: int = 1000) -> int:
    return prod(find_triplet(n))

if __name__ == '__main__':
    print(solution())