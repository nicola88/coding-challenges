"""Find any two numbers in a list adding up to a given number
Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.
For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.
Bonus: Can you do this in one pass?
"""
from typing import List


def find_addends(values: List[int], k: int):
    """
    Return the first two numbers from the list adding up to `k`
    :param values: List of numbers
    :param k: Target number
    :return: the first two numbers adding up to `k`, `None` otherwise
    """
    addends = {}
    for number in values:
        if number in addends:
            return addends[number], number
        addends[k - number] = number


assert find_addends([10, 5, 3, 7], 17) == (10, 7)
assert find_addends([10, 5, 3, 7], 15) == (10, 5)
assert find_addends([], 10) is None
assert find_addends([10], 10) is None
assert find_addends([10, 0], 10) == (10, 0)
assert find_addends([10, 5, 3, 7], 14) is None


