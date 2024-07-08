#!/usr/bin/env python3
"""This  function meatures total execution time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """computes the total_time / n"""

    begin = time.time()
    asyncio.run(wait_n(n, max_delay))
    overall_time = time.time() - begin
    return overall_time / n
