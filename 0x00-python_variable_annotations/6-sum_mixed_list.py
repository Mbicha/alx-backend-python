#!/usr/bin/env python3
"""Sum of mixed floats and elements"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_lst (list): List of mixed annotated elements
    Return:
        float: sum of elements
    """
    sum: float = 0.0
    for elm in mxd_lst:
        sum += elm
    return (sum)
