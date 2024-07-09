#!/usr/bin/env python3
"""A coroutine that collects 10 random
numbers using async comprehension"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ This coroutine collects 10 random
    numbers using async comprehension over
    async_generator"""

    return [x async for x in async_generator()]
