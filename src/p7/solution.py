import itertools

# source: https://stackoverflow.com/a/19391111
def psieve():
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:      # composite
            step = D.pop(i)
        elif i < psq:   # prime
            yield i
            continue
        else:           # composite, = p*p
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step

def solution(n: int) -> int:
    return list(itertools.islice(psieve(), n))[-1]

if __name__ == '__main__':
    print(solution(10001))