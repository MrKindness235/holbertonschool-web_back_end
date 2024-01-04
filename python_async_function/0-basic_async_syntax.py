#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
"""


import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    """This is the function that works!"""
    max_delay = random.uniform(1.0, 11.0)
    await asyncio.sleep(max_delay)
    return max_delay
