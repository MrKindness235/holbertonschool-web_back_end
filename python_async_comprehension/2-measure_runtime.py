#!/usr/bin/env python3
""" execute 4 times a function in parallell  """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute 4 times a function in parallell  """
    start = time.time()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    end = time.time() - start
    return end
