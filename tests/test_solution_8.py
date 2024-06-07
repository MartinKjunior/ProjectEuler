from ProjectEuler.src.p8.solution import *

def test_rolling_window():
    assert list(rolling_window('123456', 3)) == ['123', '234', '345', '456']
