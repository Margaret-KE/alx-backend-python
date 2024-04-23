#!/usr/bin/env python3
"""
Module with a function (couroutine) that returns
the length of delays as a list
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    run the wait_random coroutine n times
    Args:
        n (int): Refer to the previous module
        max_delay (int): Check the previous module
    Returns:
        returns a list of floats
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
