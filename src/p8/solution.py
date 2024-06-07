from collections.abc import Iterable

def load_data() -> str:
    with open('src/p8/data.txt') as f:
        return ''.join(x for x in f.read().splitlines())

def rolling_window(seq: str, width: int) -> Iterable[str]:
    """Yields a sliding window of width `width` over the sequence `seq`."""
    for i in range(len(seq) - width + 1):
        yield seq[i: i+width]

# part 5
def prod(iterable: Iterable[int], /, *, start: int = 1) -> int:
    """Returns the product of all elements in an iterable."""
    result = start
    for i in iterable:
        result *= i
    return result

def solution(n: int = 13) -> int:
    data = load_data()
    return max(
        prod(int(x) for x in window) # convert each number to int and find their product
        for window in rolling_window(data, n) # iterate over each window of width n
        if '0' not in window # ignore windows with 0 as it will always result in 0
        )

if __name__ == '__main__':
    print(solution())