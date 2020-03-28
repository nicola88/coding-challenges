"""
Given a word `W` and a list of words `[w1, w2, ..., wn]`, find two words `wi` and `wj` that appended are equal to `W`.
For example, given the word `baseball` and the list of strings `[ball, bas, base, cat]` 
you should return `base` and `ball`.
"""
from typing import List, Tuple


def split_word(word_to_split: str, words: List[str]):
    """
    Find two words in `words` that combined are equal to the `word_to_split`
    :param word_to_split: Word to split
    :param words: List of words
    :return: two words in `words` that combined are equal to the `word_to_split`, `None` otherwise
    """
    for i in range(len(word_to_split)):
        first_word = word_to_split[0:i]
        second_word = word_to_split[i:]
        if first_word in words and second_word in words:
            return first_word, second_word
    return None


assert split_word(
    "baseball", ["a", "all", "b", "ball", "bas", "base", "cat", "code", "d", "e", "quit", "z"]
) == ("base", "ball")
assert split_word(
    "skyscraper", ["scraper", "s", "sky", "scrape", "r"]
) == ("sky", "scraper")
assert split_word(
    "skyscraper", ["s", "sky", "scrape", "r"]
) is None
