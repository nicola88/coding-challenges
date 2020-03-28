from math import floor

SYMBOLS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
MAX_BASE = len(SYMBOLS) + 1
MIN_BASE = 2


def convert_to_decimal_base(value: str, input_base: int) -> int:
    """
    Convert a natural number from a numeral system base between `MIN_BASE` and `BAX_BASE` to decimal
    :param input_base: Numeral system base as integer between `MIN_BASE` and `BAX_BASE`
    :param value: number to convert to decimal base, must be a string (if not, it will be automatically converted)
    :return: Representation of the given value into decimal numeral system
    """
    assert isinstance(input_base, int), 'Base must be an integer'
    assert MIN_BASE <= input_base <= MAX_BASE, 'Base must be in [{},{}]'.format(MIN_BASE, MAX_BASE)
    if not isinstance(value, str):
        value = str(value)
    allowed_symbols = SYMBOLS[:input_base]
    decimal_value = 0
    for symbol in value:
        decimal_value *= input_base
        assert symbol in allowed_symbols, '{} symbol is not allowed in base {} numeral system'.format(symbol, input_base)
        decimal_value += allowed_symbols.index(symbol)
    return decimal_value


def convert_from_decimal_base(value: int, output_base: int) -> str:
    """
    Convert a natural number in decimal base to a numeral system base between `MIN_BASE` and `BAX_BASE`
    :param value: Natural number in decimal base
    :param output_base: a numeral system base between `MIN_BASE` and `BAX_BASE`
    :return: the given natural number expressed in the output numeral system base
    """
    assert value >= 0, "Value must be a natural number"
    assert isinstance(output_base, int), 'Base must be an integer'
    assert MIN_BASE <= output_base <= MAX_BASE, 'Base must be in [{},{}]'.format(MIN_BASE, MAX_BASE)
    allowed_symbols = SYMBOLS[:output_base]
    output_symbols = []
    quotient, remainder = value, 0
    while quotient > 0:
        remainder = quotient % output_base
        output_symbols.append(allowed_symbols[remainder])
        quotient = floor(quotient / output_base)
    output_symbols.reverse()
    return "".join(output_symbols)


def convert(input_base: int, output_base: int, value: str):
    """
    Convert a value between two numeral system base between `MIN_BASE` and `BAX_BASE`
    :param input_base: the numeral system base to convert from
    :param output_base: the numeral system base to convert to
    :param value: number to convert, must be a string (if not, it will be automatically converted)
    :return: the number converted to the output numeral system base
    """
    decimal_value = convert_to_decimal_base(value, input_base)
    return convert_from_decimal_base(decimal_value, output_base)


assert convert_to_decimal_base('3102', 4) == 210
assert convert_from_decimal_base(210, 4) == '3102'
assert convert_to_decimal_base('ab', 12) == 131
assert convert_from_decimal_base(131, 12) == 'ab'
assert convert_to_decimal_base('0', 4) == 0
