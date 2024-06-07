from ProjectEuler.src.p7.solution import *

def test_psieve():
    assert list(itertools.islice(psieve(), 10)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]