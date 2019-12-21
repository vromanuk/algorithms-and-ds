class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.set_prev(new_node)
            self.head = new_node

    def is_empty(self):
        return self.head is None

    def search(self, value):
        current = self.head
        found = False
        while current and not found:
            if current.get_value() == value:
                found = True
            else:
                current = current.get_next()
        return found

    def size(self):
        count = 0
        current = self.head
        while current:
            if current.get_value():
                count += 1
                current = current.get_next()

        return count

    def insert_after(self, index, element):
        current = self.head
        if not current:
            return
        position = 0
        while current and position <= index:
            if position == index:
                element = Node(element)
                element.set_next(current.get_next())
                element.set_prev(current)
                if current.get_next():
                    n = current.get_next()
                    n.set_prev(element)
                current.set_next(element)
                break
            else:
                current.get_next()
                position += 1

    def insert_before(self, index, element):
        current = self.head
        if not current:
            return
        position = 0
        while current and position <= index:
            if position == index:
                element = Node(element)
                element.set_next(current.get_next())
                element.set_prev(current)
                if current.get_next():
                    n = current.get_next()
                    n.set_prev(element)
                current.set_next(element)
                break
            else:
                current.get_next()
                position += 1


if __name__ == '__main__':
    double_linked_list = DoubleLinkedList()
    assert double_linked_list.is_empty() is True
    double_linked_list.add(13)
    double_linked_list.add(15)
    double_linked_list.add(88)
    assert double_linked_list.size() == 3
    assert double_linked_list.search(13) is True
    double_linked_list.insert_after(1, 23)
    assert double_linked_list.size() == 4
    double_linked_list.insert_before(2, 99)
    assert double_linked_list.size() == 5
