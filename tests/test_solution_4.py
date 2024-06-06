from ProjectEuler.src.p4.solution import *

def test_is_palindrome():
    assert is_palindrome(12321) == True
    assert is_palindrome(12345) == False

def test_find_largest_palindrome():
    assert find_largest_palindrome(2) == 9009
    assert find_largest_palindrome(3) == 906609
    assert find_largest_palindrome(4) == 99000099
    assert find_largest_palindrome(5) == 9966006699