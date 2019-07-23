from collections import deque


class Stack:
    def __init__(self, stack_items=None):
        if stack_items:
            self.stack_items = deque(stack_items)
        else:
            self.stack_items = deque()

    def push(self, value):
        self.stack_items.append(value)

    def pop(self):
        if len(self.stack_items) >= 1:
            return self.stack_items.pop()
        return

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.stack_items[-1]

    def size(self):
        return len(self.stack_items)


if __name__ == '__main__':
    print('Launching tests...')
    stack = Stack()
    test_value = 'test_value'
    new_value = 'new_value'
    assert stack.pop() is None
    assert stack.is_empty() is True
    stack.push('test_value')
    assert stack.peek() == 'test_value'
    assert stack.size() == 1
    assert stack.is_empty() is False
    stack.push('new_value')
    assert stack.pop() == new_value
    assert stack.pop() == test_value
    print('Success!')
