#!/usr/bin/env python3

"""Task 1's module."""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
     This function runs the wait_random coroutine 'n' times
    Args:
        n (int): number of times to run the coroutine
        max_delay (int): Maximum delay when running the wait_random
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
