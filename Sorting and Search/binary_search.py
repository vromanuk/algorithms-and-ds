from typing import List


def recursive_binary_search(items: List[int], target: int) -> bool:
    sorted_items = sorted(items)
    if len(sorted_items) == 0:
        return False
    else:
        middle = len(sorted_items) // 2
        if sorted_items[middle] == target:
            return True
        else:
            if target < sorted_items[middle]:
                return recursive_binary_search(sorted_items[:middle], target)
            else:
                return recursive_binary_search(sorted_items[middle + 1:], target)


def iterative_binary_search(items: List[int], target: int) -> bool:
    sorted_items = sorted(items)
    found = False
    first = 0
    last = len(sorted_items) - 1
    while first <= last and not found:
        middle = (first + last) // 2
        if sorted_items[middle] == target:
            found = True
        else:
            if target < sorted_items[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found


if __name__ == '__main__':
    list_items = [1, 2, 32, 8, 17, 19, 42, 13, 0]

    assert recursive_binary_search(list_items, 2) is True
    assert recursive_binary_search(list_items, -1) is False
    assert recursive_binary_search(list_items, 100) is False

    assert iterative_binary_search(list_items, 2) is True
    assert iterative_binary_search(list_items, -1) is False
    assert iterative_binary_search(list_items, 100) is False
