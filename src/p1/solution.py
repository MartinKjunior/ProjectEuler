"""Project Euler Problem 1: Multiples of 3 and 5."""

def list_multiples(n: int, a: int=3, b: int=5) -> list:
    """Return a list of all multiples of a or b below n."""
    return [i for i in range(1, n) if i % a == 0 or i % b == 0]

def solution_iteration(n: int=1000) -> int:
    """Return the sum of all multiples of 3 or 5 below n."""
    return sum(list_multiples(n))

def solution_math(n: int=1000) -> int:
    """Return the sum of all multiples of 3 or 5 below n."""
    n -= 1
    a, b, c = n // 3, n // 5, n // 15 #three, five, fifteen
    # sum of arithmetic series is n * (n + 1) // 2
    return 3 * a * (a + 1) // 2 + 5 * b * (b + 1) // 2 - 15 * c * (c + 1) // 2

if __name__ == "__main__":
    print(solution_iteration())
    print(solution_math())