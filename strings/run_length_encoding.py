"""
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""
import re


def encode_recursive(string: str):
    """
    Recursive implementation of run-length encoder
    :param string: Text to encode
    :return: Encoded string
    """
    if len(string) == 0:
        return ""
    char_to_encode = string[0]
    char_occurrences = 0
    for char in string:
        if char == char_to_encode:
            char_occurrences += 1
        else:
            break
    return "{}{}{}".format(
        char_occurrences, char_to_encode, encode(string[char_occurrences:])
    )


def encode(string: str):
    """
    Iterative implementation of run-length encoder
    :param string: Text to encode
    :return: Encoded string
    """
    char_to_encode = None
    char_occurrences = 0
    decoded_string = ""
    for char in string:
        if char == char_to_encode:
            char_occurrences += 1
        else:
            if char_to_encode:
                decoded_string += "{}{}".format(char_occurrences, char_to_encode)
            char_to_encode = char
            char_occurrences = 1
    if char_to_encode:
        decoded_string += "{}{}".format(char_occurrences, char_to_encode)
    return decoded_string


def decode(string: str):
    """
    Recursive implementation of run-length decoder
    :param string: Text to decode
    :return: Decoded string
    """
    i = 0
    decoded_string = ""
    while i < len(string):
        text = string[i:]
        char_occurrences = re.match(r"^\d+", text).group(0)
        offset = len(char_occurrences)
        char_to_decode = text[offset:offset + 1]
        decoded_string += char_to_decode * int(char_occurrences)
        i += offset + 1
    return decoded_string


def decode_recursive(string: str):
    """
    Iterative implementation of run-length decoder
    :param string: Text to decode
    :return: Decoded string
    """
    if len(string) < 2:
        return ""
    char_occurrences = re.match(r"^\d+", string).group(0)
    char_to_decode = string[len(char_occurrences):len(char_occurrences)+1]
    offset = len(char_occurrences) + 1
    return char_to_decode * int(char_occurrences) + decode(string[offset:])


assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"
assert decode("12A") == "AAAAAAAAAAAA"
assert encode("") == ""
assert decode("") == ""

assert encode_recursive("AAAABBBCCDAA") == "4A3B2C1D2A"
assert decode_recursive("4A3B2C1D2A") == "AAAABBBCCDAA"
assert decode_recursive("12A") == "AAAAAAAAAAAA"
assert encode_recursive("") == ""
assert decode_recursive("") == ""
