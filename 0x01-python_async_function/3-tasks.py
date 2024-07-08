#!/usr/bin/env python3
""""A function that takes an integer and returns a asyncio.Task"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task"""

    return asyncio.Task(wait_random(max_delay))
