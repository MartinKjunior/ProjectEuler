from ProjectEuler.src.p3.solution import *
from sympy import primefactors

def test_prime_factors():
    assert prime_factors(13195) == primefactors(13195) # [5, 7, 13, 29]
    assert prime_factors(600851475143) == primefactors(600851475143) # [71, 839, 1471, 6857]

def test_largest_prime_factor():
    assert largest_prime_factor(13195) == primefactors(13195)[-1] # 29
    assert largest_prime_factor(600851475143) == primefactors(600851475143)[-1] # 6857