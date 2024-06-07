def sum_of_the_squares(n: int) -> int:
    # source: https://en.wikipedia.org/wiki/Square_pyramidal_number
    return n * (n + 1) * (2 * n + 1) // 6

def square_of_the_sum(n: int) -> int:
    # source: https://en.wikipedia.org/wiki/Triangular_number
    return (n * (n + 1) // 2) ** 2

def difference(n: int) -> int:
    return square_of_the_sum(n) - sum_of_the_squares(n)

def solution(n: int = 100) -> int:
    return difference(n)

if __name__ == '__main__':
    print(solution())