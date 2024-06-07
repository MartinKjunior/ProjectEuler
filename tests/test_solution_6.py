from ProjectEuler.src.p6.solution import *

def test_sum_of_the_squares():
    assert sum_of_the_squares(10) == 385
    assert sum_of_the_squares(100) == 338350

def test_square_of_the_sum():
    assert square_of_the_sum(10) == 3025
    assert square_of_the_sum(100) == 25502500