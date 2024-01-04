#!/usr/bin/env python3
"""Experimental function that uses the last task's basis to expand upon."""


from typing import List
task_wait_random = __import__('4-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that repeats wait_random (n) times."""
    lista = []
    for _ in range(0, n):
        lista.append(await task_wait_random(max_delay))
    return sorted(lista)
