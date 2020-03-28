"""
Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.
For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
you should return the following:
```
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
```
"""
from functools import reduce
from math import floor
from typing import List


def justify_line(words: List[str], length: int) -> str:
    """
    Justify a line containing the given words
    :param words: Words of the line
    :param length: Fixed length of the justified line
    :return: Justified line
    """
    assert len(words) > 0
    total_spaces = length - len(reduce(lambda x, y: x + y, words))
    spaces_between_words = floor(total_spaces / (len(words) - 1))
    padding = total_spaces - spaces_between_words * (len(words) - 1)
    string = " " * padding + (" " * spaces_between_words).join(words)
    return string


def justify_text(words: List[str], fixed_line_length: int):
    """
    Justify given text
    :param words: List of words
    :param fixed_line_length: Fixed length of each line
    :return: Justified text
    """
    current_line_length = 0
    current_line_words = []
    lines = []
    for word in words:
        required_space = len(word) + 1
        if current_line_length + required_space > fixed_line_length:
            lines.append(justify_line(current_line_words, fixed_line_length))
            current_line_length = 0
            current_line_words = []
        current_line_words.append(word)
        current_line_length += required_space
    if len(words) > 0:
        lines.append(justify_line(current_line_words, fixed_line_length))
    return lines


w = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16
justified_text = justify_text(w, k)
assert len(justified_text) == 3
assert justified_text[0] == " the quick brown"
assert justified_text[1] == "fox  jumps  over"
assert justified_text[2] == "the   lazy   dog"
