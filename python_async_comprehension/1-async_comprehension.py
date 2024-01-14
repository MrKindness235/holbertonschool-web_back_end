#!/usr/bin/env python3
""" collect a list of numbers asynchronously geenerated """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ collect a list of numbers asynchronously geenerated """
    result = [i async for i in async_generator()]
    return result
