#!/usr/bin/env python3
""""""


import asyncio
import random


async def wait_random(max_delay: float = 10) -> float:
    max_delay = random.uniform(1.0, 11.0)
    await asyncio.sleep(max_delay)
    return max_delay
