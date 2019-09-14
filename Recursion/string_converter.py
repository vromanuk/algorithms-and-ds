def to_str(n: int, base: int) -> str:
    convert_string = '0123456789ABCDEF'
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


if __name__ == '__main__':
    assert to_str(1453, 16) == '5AD'
