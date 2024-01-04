#!/usr/bin/env python3
"""Experimental function that uses the last task's basis to expand upon."""


import random
wait_random = __import__('0-basic_async_syntax').wait_random


def bubbleSort(array):
    """
    Holberton expects to do order the last list without using sort().
    Implementation taken from: https://www.programiz.com/dsa/bubble-sort
    """

    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


async def wait_n(n: int, max_delay: int) -> list:
    """Function that repeats wait_random (n) times."""
    lista = []
    for i in range(0, n):
        lista.append(await wait_random(max_delay))
    bubbleSort(lista)
    return lista
