#!/usr/bin/env python3
"""Tuple of string and square of int/float"""


from typing import Tuple


def to_kv(k: str, v: Tuple[int, float]) -> Tuple[str, float]:
    """
    Args:
        k (str): String
        v (int/float): Integer or float
    Return:
        tuple: First element is a string and second float
    """
    return (k, v**2)
