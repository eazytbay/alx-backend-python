#!/usr/bin/env python3
"""Definition of a type-annotated function `safely_get_value`"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    '''Retrieves a value from a dict using a given key.'''
    if key in dct:
        return dct[key]
    else:
        return default
