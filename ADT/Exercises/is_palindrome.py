from ADT.stack import Stack


def is_palindrome(string):
    flag = True
    if not isinstance(string, str):
        raise ValueError
    stack = Stack(string)
    for _ in string:
        if _ == stack.pop():
            continue
        else:
            flag = False

    return flag


if __name__ == '__main__':
    assert is_palindrome('madam') is True
