from ProjectEuler.src.p5.solution import *

def test_minimum_required_prime_factors():
    assert minimum_required_prime_factors(10) == {2: 3, 3: 2, 5: 1, 7: 1}
    assert minimum_required_prime_factors(20) == {2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}
    assert minimum_required_prime_factors(30) == {2: 4, 3: 3, 5: 2, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1}

def test_primes_to_list():
    assert primes_to_list({2: 3, 3: 2, 5: 1, 7: 1}) == [2, 2, 2, 3, 3, 5, 7]
    assert primes_to_list({2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}) == [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
    assert primes_to_list({2: 4, 3: 3, 5: 2, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1}) == [2, 2, 2, 2, 3, 3, 3, 5, 5, 7, 11, 13, 17, 19, 23, 29]

def test_prod():
    assert prod([1, 2, 3, 4, 5]) == 120
    assert prod([1, 2, 3, 4, 5], start=2) == 240
    assert prod({1, 2, 3, 4, 5}) == 120
    assert prod((x for x in range(1, 6))) == 120