from typing import List


def linear_search_for_loop(items: List[int], target: int) -> bool:
    found = False
    for item in items:
        if item == target:
            found = True
            break
    return found


def linear_search_with_while(items: List[int], target: int) -> bool:
    found = False
    position = 0
    length = len(items)
    while position < length and not found:
        if target == items[position]:
            found = True
        else:
            position += 1

    return found


if __name__ == '__main__':
    list_items = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    assert linear_search_for_loop(list_items, 2) is True
    assert linear_search_for_loop(list_items, -1) is False
    assert linear_search_with_while(list_items, 0) is True
    assert linear_search_with_while(list_items, 23) is False
