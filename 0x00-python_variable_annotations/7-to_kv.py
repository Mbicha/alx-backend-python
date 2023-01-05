#!/usr/bin/env python3
"""Tuple of string and square of int/float"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k (str): String
        v (int/float): Integer or float
    Return:
        tuple: First element is a string and second float
    """
    ans: Tuple(str, Union[int, float])
    ans = (k, v**2)
    return (ans)
