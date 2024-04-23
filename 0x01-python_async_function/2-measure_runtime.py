#!/usr/bin/env python3

"""
Module with a function that creates a task
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    wait for a random number of some seconds
    and return an asyncio Task
    Args:
        max_delay (int): maximum number of seconds
        to wait
    Returns:
        returns an asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))
