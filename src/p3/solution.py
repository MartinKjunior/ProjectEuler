from sympy import primefactors

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

def prime_factors_sympy(n: int) -> list[int]:
    return primefactors(n)

def largest_prime_factor(n: int) -> int:
    """Returns the largest prime factor of n."""
    i = 2
    # The largest prime factor of n must be less than sqrt(n).
    while i ** 2 < n:
        # If there are multiple of the same prime factor, divide them out.
        while n % i == 0:
            n //= i
        i += 1
    return n

def solution(n: int) -> int:
    return largest_prime_factor(n)

if __name__ == '__main__':
    print(solution(600851475143))