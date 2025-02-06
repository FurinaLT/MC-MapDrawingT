"""
定义迭代(生成)器
"""

from . import BOX_CAPACITY
from .constructor import Box, Map  # pylint: disable = R0401


def iterator(Begin: int, End: int) -> list[Map | Box]:
    """
    迭代(生成)器
    通过传入左闭右开区间得到对象
    :param Begin: 地图起始编号
    :param End: 地图结束编号
    :return: 装有 Map/Box 对象的列表
    """
    from math import ceil, log

    step = BOX_CAPACITY ** ceil(log(End - Begin, 27) - 1) if End - Begin > 1 else 1

    seq = list(range(Begin, End, step)) + [End]
    return [
        (Map(i, seq[i]) if seq[i + 1] - seq[i] == 1 else Box(seq[i], seq[i + 1], i))
        for i in range(len(seq) - 1)
    ]
