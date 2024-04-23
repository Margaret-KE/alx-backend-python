#!/usr/bin/env python3

"""Task 1"""

from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns some 10 random numbers based on the
    other function defined in the previous module
    """
    return [num async for num in async_generator()]
