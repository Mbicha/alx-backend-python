#!/usr/bin/env python3
"""Sum of list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list (list): List of floats
    Return:
        float: sum of list elaments
    """
    sum: float = 0.0
    for i in input_list:
        sum += i

    return (sum)
