#!/usr/bin/env python3
"""Type checking"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Args:
        lst: Tuple of numbers
        factor: increase factor

    Return:
        zoomed
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
