from functools import lru_cache
from typing import Generator


@lru_cache(maxsize=None)
def rec_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)


def fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        raise ValueError('Incorrect input')
    current, nxt = 0, 1
    while n >= 1:
        current, nxt = nxt, current + nxt
        n -= 1
    return current


def gen_fibonacci() -> Generator[int, None, None]:
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


if __name__ == '__main__':
    assert rec_fibonacci(1) == 1
    assert rec_fibonacci(10) == 55

    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
