#!/usr/bin/env python3
"""Task 2's module."""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the excetution time of a subroutine
    Args:
        n (int): number of times to run the subroutine
        max_delay (int): maximum amout of time to delay
    Returns:
        returns a float
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
