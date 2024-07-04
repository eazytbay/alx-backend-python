#!/usr/bin/env python3
"""Definition a type-annotated function for Task 12."""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Establishes multiple copies of items in a tuple, @lst."""
    zoomed_in: List = [
        item for item in lst
        for x in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
