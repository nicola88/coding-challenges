"""Given an encoded message and a mapping, count the number of ways it can be decoded
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
TODO Follow-up: return all possible ways the message can be decoded, instead of simply count them
"""


def decode_message(message: str) -> int:
    return __count_decoding(message) if message is not None else 0


def __count_decoding(message: str) -> int:
    """
    Count the number of ways the given message can be decoded
    :param message: Message
    :return: the number of ways the given message can be decoded
    """
    if len(message) == 0:
        return 1
    decoded_values = 0
    for i in range(27):
        encoded_value = str(i)
        if message.startswith(encoded_value):
            decoded_values += __count_decoding(message[len(encoded_value):])
    return decoded_values


assert decode_message('111') == 3
assert decode_message('26') == 2
assert decode_message('232') == 2
assert decode_message('') == 1
assert decode_message(None) == 0
