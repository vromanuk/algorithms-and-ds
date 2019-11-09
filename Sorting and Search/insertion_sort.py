from typing import List


def insertion_sort(numbers: List[int]):
    length = len(numbers)
    for index in range(1, length):
        current = numbers[index]
        position = index
        while position > 0 and numbers[position - 1] > current:
            numbers[position] = numbers[position - 1]
            position -= 1
        numbers[position] = current


if __name__ == '__main__':
    unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_list = sorted(unsorted_list)
    insertion_sort(unsorted_list)
    assert sorted_list == unsorted_list
