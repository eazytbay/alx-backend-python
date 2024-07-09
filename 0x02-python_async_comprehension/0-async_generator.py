#!/usr/bin/env python3
"""This is an async generator that loops 10 times"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ This Loops 10 times and then waits 1 second
    to yield a random number between 0 and 10"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
