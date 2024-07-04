#!/usr/bin/env python3
"""This function takes a multiplier and returns a function
that multiplies a float by multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that multiplies a float
    by multiplier is returned"""
    def inner_function(number: float) -> float:
        """The inner function multiplies the two nums"""
        return multiplier * number
    return inner_function
