#!/usr/bin/env python3
"""A function that measures total execution time for wait_n"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """list of the delays sorted in ascending order is returned"""

    resp_time: List[float] = [wait_random(max_delay) for _ in range(n)]
    rslt = await asyncio.gather(*resp_time)
    return sorted(rslt)
