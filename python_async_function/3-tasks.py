#!/usr/bin/env python3
"""This is very confusing so I will NOT explain; enjoy."""
import asyncio
wait_random = __import__('0-basic_async_syntax')


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Converts random to Task."""
    return asyncio.create_task(wait_random(max_delay))
