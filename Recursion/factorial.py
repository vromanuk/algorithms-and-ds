def rec_factorial(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        raise ValueError('Factorial does not exist for negative numbers')
    elif n == 1:
        return 1
    return n * rec_factorial(n - 1)


def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError
    result = 1
    while n != 1:
        result *= n
        n -= 1

    return result


if __name__ == '__main__':
    assert rec_factorial(1) == 1
    assert rec_factorial(5) == 120
    assert rec_factorial(6) == 720
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720
