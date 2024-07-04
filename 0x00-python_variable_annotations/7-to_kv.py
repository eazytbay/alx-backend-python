#!/usr/bin/env python3
""" This function returns a
tuple when given different inputs"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """k and square of v is returned in a tuple"""

    return tuple([k, v * v])
