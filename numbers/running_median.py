"""Compute the running median of a sequence of numbers
That is, given a stream of numbers, return the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence `[2, 1, 5, 7, 2, 0, 5]`, your algorithm should return `[2, 1.5, 2, 3.5, 2, 2.0, 2]`.
"""
from math import floor, ceil
from typing import List


def running_median(numbers: List[float]):
    """
    Compute the running median of a sequence of numbers.
    :param numbers: List of numbers
    :return: the running median of the given numbers.
    """
    running_medians = []
    for i in range(len(numbers)):
        running_size = i + 1
        sorted_numbers = sorted(numbers[:running_size])
        if running_size % 2 == 0:  # even-numbered sublist
            first, second = sorted_numbers[floor(i / 2)], sorted_numbers[ceil(i / 2)]
            running_medians.append((first + second) / 2)
        else:  # odd-numbered sublist
            running_medians.append(sorted_numbers[int(i/2)])
    return running_medians


assert running_median([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2.0, 2]
