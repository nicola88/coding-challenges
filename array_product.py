"""Map an array so that each element is the product of all the other elements
Given an array of integers, return a new array such that each element at index `i` of the new array is the product
of all the numbers in the original array except the one at `i`.
For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`.
If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.
Follow-up: what if you can't use division?
"""
from functools import reduce
from typing import List


def get_array_product(values: List[int]) -> List[int]:
    """
    Map each element of the original array to the product of the other elements of the array
    > This version uses division and requires `O(1)` auxiliary space
    :param values: List of integers
    :return: a new array where each element is the product of all `values` except the one at same position
    """
    original_product = reduce(lambda x, y: x * y, values)
    return [int(original_product / v) for v in values]


def get_array_product_v2(values: List[int]) -> List[int]:
    """
    Map each element of the original array to the product of the other elements of the array
    > This version does not use division and requires `O(n)` auxiliary space
    :param values: List of integers
    :return: a new array where each element is the product of all `values` except the one at same position
    """
    size = len(values)
    left = [1] * size
    right = [1] * size
    for i in range(1, size):
        left[i] = values[i - 1] * left[i - 1]
    for i in range(size - 2, -1, -1):
        right[i] = values[i + 1] * right[i + 1]
    return [left[i] * right[i] for i in range(size)]


def get_array_product_v3(values: List[int]) -> List[int]:
    """
    Map each element of the original array to the product of the other elements of the array
    > This version does not use division and requires `O(1)` auxiliary space
    :param values: List of integers
    :return: a new array where each element is the product of all `values` except the one at same position
    """
    size = len(values)
    left = 1
    right = 1
    product = [1] * size
    for i in range(1, size):
        left = values[i - 1] * left
        product[i] *= left
    for i in range(size - 2, -1, -1):
        right = values[i + 1] * right
        product[i] *= right
    return product


input_array = [1, 2, 3, 4, 5]
output_array = [120, 60, 40, 30, 24]
assert get_array_product(input_array) == output_array
assert get_array_product_v2(input_array) == output_array
assert get_array_product_v3(input_array) == output_array

input_array = [3, 2, 1]
output_array = [2, 3, 6]
assert get_array_product(input_array) == output_array
assert get_array_product_v2(input_array) == output_array
assert get_array_product_v3(input_array) == output_array
