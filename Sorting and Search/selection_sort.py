import random

from typing import List


def selection_sort(numbers: List[int]):
    length = len(numbers) - 1
    for slot in range(length, 0, -1):
        position_of_max = 0
        for location in range(1, slot + 1):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location
        numbers[slot], numbers[position_of_max] = numbers[position_of_max], numbers[slot]


def selection_sort_with_min(numbers: List[int]):
    length = len(numbers)
    for i in range(length):
        min_index = numbers.index(min(numbers[i:]))
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]


if __name__ == '__main__':
    unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_list = sorted(unsorted_list)
    selection_sort(unsorted_list)
    assert sorted_list == unsorted_list
    random.shuffle(unsorted_list)
    selection_sort_with_min(unsorted_list)
    assert sorted_list == unsorted_list
