#!/usr/bin/env python3
"""function that measures time."""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Time measuring function."""
    total_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - total_time
    return total_time / n
