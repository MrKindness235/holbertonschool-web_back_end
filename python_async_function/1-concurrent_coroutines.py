#!/usr/bin/env python3
"""Experimental function that uses the last task's basis to expand upon."""


from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that repeats wait_random (n) times."""
    lista = []
    for _ in range(0, n):
        lista.append(await wait_random(max_delay))
    return sorted(lista)
