"""Count in how many unique ways you can climb a staircase
There exists a staircase with `N` steps, and you can climb up either 1 or 2 steps at a time.
Given `N`, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.
For example, if `N` is 4, then there are 5 unique ways:
- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2

What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers `X`?
For example, if `X = {1, 3, 5}`, you could climb 1, 3, or 5 steps at a time.
"""
from typing import List


def __climb(remaining_steps: int, possible_steps: List[int]) -> int:
    """
    Return the number of unique ways to climb `remaining_steps` steps doing any of `possible_steps` at a time
    :param remaining_steps: Number of steps to climb
    :param possible_steps: Number of steps you can climb at a time
    :return: the number of unique ways to climb the remaining steps of the staircase
    """
    if remaining_steps == 0:
        return 1
    if remaining_steps < 0:
        return 0
    ways_count = 0
    for step in possible_steps:
        ways_count += __climb(remaining_steps - step, possible_steps)
    return ways_count


def climb_staircase(total_steps: int, steps_at_time: List[int]):
    """
    Return the number of unique ways to climb a staircase of `total_total_steps` steps, `possible_steps` steps at a time
    :param total_steps: Total number of steps
    :param steps_at_time: Number of steps you can climb at a time
    :return: the number of unique ways to climb the staircase
    """
    return __climb(total_steps, steps_at_time)


assert climb_staircase(1, [2]) == 0
assert climb_staircase(4, [1, 2]) == 5
assert climb_staircase(5, [1, 3, 5]) == 5
assert climb_staircase(6, [1, 3, 5]) == 8
