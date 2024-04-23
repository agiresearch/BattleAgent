import collections

import roman
from procoder.utils.my_typing import *

# from .base import Module, T, TS, as_module


def make_ordered_dict(names, values):
    return collections.OrderedDict(zip(names, values))


def number_indexing(i: int) -> str:
    return f"{i + 1}. "


def letter_indexing(i: int) -> str:
    return f"{chr(ord('a') + i)}. "


def uppercase_letter_indexing(i: int) -> str:
    return f"{chr(ord('A') + i)}. "


def roman_numeral_indexing(i: int) -> str:
    return f"{roman.toRoman(i + 1)}. "


def star_indexing(i: int) -> str:
    return "* "


def dash_indexing(i: int) -> str:
    return "- "


def get_sharp_indexing(n: int) -> Callable[[int], str]:
    return lambda i: "#" * n + " "


def get_equal_indexing(n: int) -> Callable[[int], str]:
    return lambda i: "=" * n + " "


sharp1_indexing = get_sharp_indexing(1)
sharp2_indexing = get_sharp_indexing(2)
sharp3_indexing = get_sharp_indexing(3)
sharp4_indexing = get_sharp_indexing(4)

equal2_indexing = get_equal_indexing(2)
equal3_indexing = get_equal_indexing(3)
equal4_indexing = get_equal_indexing(4)
