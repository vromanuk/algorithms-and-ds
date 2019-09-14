"""
Sum of elements without while and for loops.
"""


def listsum(numbers: list) -> int:
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + listsum(numbers[1:])


if __name__ == '__main__':
    nums: list = [1, 3, 5, 7, 9]
    assert listsum(nums) == 25
