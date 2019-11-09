from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result


def merge_sort(numbers: List[int]) -> List[int]:
    length = len(numbers)
    if length <= 1:
        return numbers
    else:
        left = numbers[:length // 2]
        right = numbers[length // 2:]
    return merge(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    sorted_list = sorted(unsorted_list)
    merged_sort_list = merge_sort(unsorted_list)
    assert sorted_list == merged_sort_list
