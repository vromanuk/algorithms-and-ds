import operator

from ADT.stack import Stack

ops: dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def evaluate_postfix(expression: str) -> int:
    stack = Stack()
    if not isinstance(expression, str):
        raise ValueError('Incorrect value')
    tokens = expression.split()
    for token in tokens:
        if token in ops:
            first_item = stack.pop()
            second_item = stack.pop()
            stack.push(ops[token](first_item, second_item))
        else:
            stack.push(int(token))
    return stack.pop()


if __name__ == '__main__':
    print('RUN TESTS')
    assert evaluate_postfix('1 2 + ') == 3
    assert evaluate_postfix('990 1 2 + *') == 2970
    assert evaluate_postfix('1000 990 1 2 + * +') == 3970
    print('TEST SUCCESSFULLY RUN')
