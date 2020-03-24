"""
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""


def balanced_parenthesis(string: str):
    """

    :param string: a string of round, curly, and square open and closing brackets
    :return: whether the brackets are balanced (well-formed)
    :raises ValueError: if the string contains a character which is not a parenthesis
    """
    stack = []
    matching_parenthesis = {')': '(', ']': '[', '}': '{'}
    open_parenthesis = {'(', '[', '{'}
    close_parenthesis = {')', ']', '}'}
    for parenthesis in string:
        if parenthesis in open_parenthesis:
            stack.append(parenthesis)
        elif parenthesis in close_parenthesis:
            if len(stack) == 0 or stack[-1] != matching_parenthesis[parenthesis]:
                return False
            stack.pop()
        else:
            raise ValueError("The input string contains a character which is not a parenthesis: " + parenthesis)
    return len(stack) == 0


assert balanced_parenthesis("") is True
assert balanced_parenthesis("([])[]({})") is True
assert balanced_parenthesis("([)]") is False
assert balanced_parenthesis("((()") is False
