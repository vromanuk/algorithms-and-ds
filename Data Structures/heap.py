"""
Implementation of a priority queue. An array, visualized as a nearly complete binary tree.
"""


class BinaryHeap:
    def __init__(self):
        self._heap = [0]
        self._size = 0

    def heapify_up(self, i: int) -> None:
        while i // 2 > 0:
            if self._heap[i] < self._heap[i // 2]:  # i//2 => parent node
                self._heap[i // 2], self._heap[i] = self._heap[i], self._heap[i // 2]
            i = i // 2

    def heapify_down(self, i: int) -> None:
        while (i * 2) <= self._size:  # i*2 => left child
            min_child_idx = self.get_min_child_idx(i)
            if self._heap[i] > self._heap[min_child_idx]:
                self._heap[i], self._heap[min_child_idx] = self._heap[min_child_idx], self._heap[i]
            i = min_child_idx

    def insert(self, element: int) -> None:
        self._heap.append(element)
        self._size += 1
        self.heapify_up(self._size)

    def get_min_child_idx(self, i):
        if i * 2 + 1 > self._size:
            return i * 2
        else:
            if self._heap[i * 2] < self._heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def remove_min(self) -> int:
        min_value = self._heap[1]
        self._heap[1] = self._heap[self._size]
        self._size -= 1
        self._heap.pop()
        self.heapify_down(1)
        return min_value

    def build_heap(self, _list: list) -> None:
        length = len(_list)
        i = length // 2
        self._size = length
        self._heap = [0] + _list[:]
        while i > 0:
            self.heapify_down(i)
            i -= 1


class PriorityQueue(BinaryHeap):
    def __init__(self, values: list):
        super().__init__()
        self._binary_heap = BinaryHeap()
        self._binary_heap.build_heap(values)

    @property
    def min_v(self):
        return self._binary_heap._heap[1]

    def extract_min(self):
        return self._binary_heap.remove_min()


if __name__ == '__main__':
    binary_heap = BinaryHeap()
    binary_heap.build_heap([9, 5, 6, 2, 3])
    print(binary_heap.remove_min())
    print(binary_heap.remove_min())
    print(binary_heap.remove_min())
    print(binary_heap.remove_min())
    print(binary_heap.remove_min())
    priority_queue = PriorityQueue([9, 5, 6, 2, 3])
    print(priority_queue.min_v)
    print(priority_queue.extract_min())
    print(priority_queue.min_v)
