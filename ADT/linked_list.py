class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_data(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return f'{self.head}'

    def search(self, search_value):
        current = self.head
        found = False
        while current and not found:
            if current.get_value() == search_value:
                found = True
            else:
                current = current.get_next()

        return found

    def delete(self, value):
        found = False
        current = self.head
        previous = None
        while current and not found:
            if current.get_value() == value:
                found = True
            else:
                previous = current
                current = current.get_next()
        if not previous:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def add(self, value):
        val = Node(value)
        val.set_next(self.head)
        if not self.head:
            self.head = val
            self.tail = self.head
        else:
            self.head = val

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()

        return count

    def append(self, value):
        if not self.head:
            self.add(value)
        val = Node(value)
        self.tail.set_next(val)
        self.tail = val


if __name__ == '__main__':
    print('Run Tests')
    node1 = Node(12)
    node2 = Node(99)
    node3 = Node(37)
    assert node1.get_value() == 12

    linked_list = LinkedList()
    linked_list.add(22)
    linked_list.add(31)
    linked_list.add(64)
    linked_list.add(88)
    linked_list.add(93)
    linked_list.add(26)
    linked_list.add(54)

    assert linked_list.size() == 7
    assert linked_list.search(31) is True
    assert linked_list.search(100) is False
    linked_list.append(13)
    assert linked_list.tail.value == 13
    assert linked_list.size() == 8
    linked_list.delete(22)
    assert linked_list.search(22) is False
    assert linked_list.size() == 7
    print('Tests successfully run!')
