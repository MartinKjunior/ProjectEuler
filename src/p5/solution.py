from collections.abc import Iterable

# part 3
def prime_factors(n: int) -> list[int]:
    """Returns a list of prime factors of n."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor += 1
    return factors

def minimum_required_prime_factors(n: int) -> dict[int, int]:
    """Returns the largest prime factor count for each number up to n.
    e.g. minimum_prime_factors(10) == {2: 3, 3: 2, 5: 1, 7: 1}"""
    result = {}
    for i in range(2, n+1):
        primes = prime_factors(i)
        for n in set(primes):
            result[n] = max(result.get(n, 0), primes.count(n))
    return result

def primes_to_list(dictionary: dict[int, int]) -> list[int]:
    """Returns a list of prime numbers from a dictionary of prime factors."""
    result = []
    for prime, count in dictionary.items():
        result.extend([prime] * count)
    return result

def prod(iterable: Iterable[int], /, *, start: int = 1) -> int:
    """Returns the product of all elements in an iterable."""
    result = start
    for i in iterable:
        result *= i
    return result

def smallest_multiple(n: int) -> int:
    """Returns the smallest number that is evenly divisible by all numbers up to n."""
    return prod(primes_to_list(minimum_required_prime_factors(n)))

def solution(n: int = 20) -> int:
    """The smallest number evenly divisible by all numbers up to n is the multiple of its prime factors. 
    However, numbers like 8 require more than one factor of 2, therefore we need to find the minimum
    number of each prime factor that makes up the final number."""
    return smallest_multiple(n)

if __name__ == '__main__':
    print(solution())

# faster solution, credit: https://stackoverflow.com/a/67800337
def gcd(a, b):
    big, small = (a, b) if a > b else (b, a)
    while True:
        if big % small == 0:
            return small
        else:
            rem = big % small
            big = small
            small = rem

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(n):
    spn = 1  # smallest positive number
    for i in range(1, n + 1):
        spn = lcm(spn, i)
    return int(spn)