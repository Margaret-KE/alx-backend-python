#!/usr/bin/env python3

"""Task 0's module."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
     This couroutine waits for a random number of seconds
    and returns the number of seconds waited
    Args:
        max_delay (int): Maximum delay
    Returns:
        returns a float
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
