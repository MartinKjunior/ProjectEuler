import pytest
from ProjectEuler.src.p1.solution import *

@pytest.mark.parametrize("input,expected", [
    (( 7, 3, 5), [3, 5, 6]),
    ((10, 3, 5), [3, 5, 6, 9]),
    ((12, 2, 7), [2, 4, 6, 7, 8, 10]),
])
def test_list_multiples(input, expected):
    assert list_multiples(*input) == expected

def test_solution():
    assert solution_iteration(10) == 23
    assert solution_iteration(1000) == 233168
    assert solution_math(10) == 23
    assert solution_math(1000) == 233168