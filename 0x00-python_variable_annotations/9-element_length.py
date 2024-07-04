#!/usr/bin/env python3
"""Duck annotation of a typed iterable object"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returning the appropriate types"""
    return [(i, len(i)) for i in lst]
