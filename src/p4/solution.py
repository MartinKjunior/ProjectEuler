def is_palindrome(a: int|str) -> bool:
    return str(a) == str(a)[::-1]

def find_largest_palindrome(digits: int = 3) -> int:
    _max = 10 ** digits
    largest = 0
    # count down from _max
    for i in range(_max, 0, -1):
        for j in range(_max, 0, -1):
            num = i * j
            # if num is less than the largest palindrome found so far, the rest of the loop will not find a larger palindrome
            if num < largest:
                break
            # all palindromes with an even number of digits are divisible by 11
            # https://math.stackexchange.com/questions/985345/proving-a-palindromic-integer-with-an-even-number-of-digits-is-divisible-by-11
            if digits % 2 == 0 and num % 11 != 0:
                continue
            if is_palindrome(num):
                largest = num
    return largest

def solution(digits: int = 3) -> int:
    return find_largest_palindrome(digits)

if __name__ == '__main__':
    print(solution())