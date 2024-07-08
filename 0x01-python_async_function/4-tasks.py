#!/usr/bin/env python3
"""Implementation of a closely identical wait_n function"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """a modified implementation of wait_n
    """

    rslt = await asyncio.gather(*tuple(map(lambda _: task_wait_random(
        max_delay), range(n))))
    return sorted(rslt)
