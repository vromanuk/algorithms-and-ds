from typing import List


def bubble_sort(numbers: List[int]):
    exchanges = True
    length = len(numbers) - 1
    while length > 0 and exchanges:
        exchanges = False
        for i in range(length):
            if numbers[i] > numbers[i + 1]:
                exchanges = True
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        length -= 1


if __name__ == '__main__':
    unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_list = sorted(unsorted_list)
    bubble_sort(unsorted_list)
    assert sorted_list == unsorted_list
