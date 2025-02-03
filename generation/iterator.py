from . import BOX_CAPACITY
from .constructor import Box, Map


def iterator(Begin: int, End: int) -> list[Map | Box]:
    from math import ceil, log

    step = BOX_CAPACITY ** ceil(log(End - Begin, 27) - 1) if End - Begin > 1 else 1

    seq = list(range(Begin, End, step)) + [End]
    return [
        (Map(i, seq[i]) if seq[i + 1] - seq[i] == 1 else Box(seq[i], seq[i + 1], i))
        for i in range(len(seq) - 1)
    ]
