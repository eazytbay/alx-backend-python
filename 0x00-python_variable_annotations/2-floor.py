#!/usr/bin/env python3
"""annotated implementation of floor"""


def floor(n: float) -> int:
    """function implementation"""

    return int(n - (n % 1))
