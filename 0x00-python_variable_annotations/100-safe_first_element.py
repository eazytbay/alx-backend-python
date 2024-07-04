#!/usr/bin/env python3
"""To Augment the given code
with duck-typed annotations"""


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
