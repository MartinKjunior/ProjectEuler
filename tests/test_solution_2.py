from ProjectEuler.src.p2.solution import *

def test_fib_recursive():
    assert fib_recursive(0) == 1
    assert fib_recursive(1) == 1
    assert fib_recursive(2) == 2
    assert fib_recursive(3) == 3
    assert fib_recursive(4) == 5
    assert fib_recursive(5) == 8
    assert fib_recursive(6) == 13
    assert fib_recursive(7) == 21
    assert fib_recursive(8) == 34
    assert fib_recursive(9) == 55
    assert fib_recursive(10) == 89

def test_fib_closed():
    assert fib_closed(0) == 1
    assert fib_closed(1) == 1
    assert fib_closed(2) == 2
    assert fib_closed(3) == 3
    assert fib_closed(4) == 5
    assert fib_closed(5) == 8
    assert fib_closed(6) == 13
    assert fib_closed(7) == 21
    assert fib_closed(8) == 34
    assert fib_closed(9) == 55
    assert fib_closed(10) == 89

def test_fib_iterative():
    assert fib_iterative(0) == 1
    assert fib_iterative(1) == 1
    assert fib_iterative(2) == 2
    assert fib_iterative(3) == 3
    assert fib_iterative(4) == 5
    assert fib_iterative(5) == 8
    assert fib_iterative(6) == 13
    assert fib_iterative(7) == 21
    assert fib_iterative(8) == 34
    assert fib_iterative(9) == 55
    assert fib_iterative(10) == 89

def test_fib_recursive_vs_closed():
    for n in range(11):
        assert fib_recursive(n) == fib_closed(n)

def test_fib_recursive_large():
    assert fib_recursive(49) == 12586269025

def test_fib_closed_large():
    assert fib_closed(49) == 12586269025

def test_fib_iterative_large():
    assert fib_iterative(49) == 12586269025
    assert fib_iterative(299) == 222232244629420445529739893461909967206666939096499764990979600
    assert fib_iterative(999) == 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

def test_fib_list():
    assert fib_list(0) == []
    assert fib_list(1) == [1]
    assert fib_list(2) == [1, 1]
    assert fib_list(3) == [1, 1, 2]
    assert fib_list(4) == [1, 1, 2, 3]
    assert fib_list(5) == [1, 1, 2, 3, 5]
    assert fib_list(6) == [1, 1, 2, 3, 5, 8]
    assert fib_list(7) == [1, 1, 2, 3, 5, 8, 13]
    assert fib_list(8) == [1, 1, 2, 3, 5, 8, 13, 21]
    assert fib_list(9) == [1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fib_list(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_fib_list_max():
    assert fib_list_max(0) == []
    assert fib_list_max(1) == [1, 1]
    assert fib_list_max(2) == [1, 1, 2]
    assert fib_list_max(3) == [1, 1, 2, 3]
    assert fib_list_max(4) == [1, 1, 2, 3]
    assert fib_list_max(5) == [1, 1, 2, 3, 5]
    assert fib_list_max(6) == [1, 1, 2, 3, 5]
    assert fib_list_max(7) == [1, 1, 2, 3, 5]
    assert fib_list_max(8) == [1, 1, 2, 3, 5, 8]
    assert fib_list_max(9) == [1, 1, 2, 3, 5, 8]
    assert fib_list_max(10) == [1, 1, 2, 3, 5, 8]
    assert fib_list_max(11) == [1, 1, 2, 3, 5, 8]
    assert fib_list_max(12) == [1, 1, 2, 3, 5, 8]
    assert fib_list_max(13) == [1, 1, 2, 3, 5, 8, 13]
    assert fib_list_max(14) == [1, 1, 2, 3, 5, 8, 13]

def test_fib_list_even_max():
    assert fib_list_even_max(0) == []
    assert fib_list_even_max(1) == []
    assert fib_list_even_max(2) == [2]
    assert fib_list_even_max(3) == [2]
    assert fib_list_even_max(8) == [2, 8]
    assert fib_list_even_max(9) == [2, 8]

def test_solution():
    assert solution(0) == 0
    assert solution(1) == 0
    assert solution(2) == 2
    assert solution(3) == 2
    assert solution(4_000_000) == 4613732