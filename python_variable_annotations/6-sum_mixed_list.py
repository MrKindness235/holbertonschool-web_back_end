#!/usr/bin/env python3
"""type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Adds all elements of given list
    which is a mixed list of INTs and FLOATs"""
    return sum(mxd_lst)
