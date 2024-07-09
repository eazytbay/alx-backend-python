#!/usr/bin/env python3
""" write a measure_runtime coroutine
that will execute async_comprehension
four times in parallel using asyncio. gather
"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of parallel coroutines"""
    begin = time()
    await asyncio.gather(*(async_comprehension() for x in range(4)))
    return time() - begin
