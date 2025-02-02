from . import BOX_CAPACITY
from .constructor import Box, Map


def Iterator(Begin: int, End: int) -> list[Map | Box]:
    from math import ceil, log

    Step = BOX_CAPACITY ** ceil(log(End - Begin, 27) - 1) if End - Begin > 1 else 1

    Sequence = list(range(Begin, End, Step)) + [End]
    return list(
        (
            Map(i, Sequence[i])
            if Sequence[i + 1] - Sequence[i] == 1
            else Box(Sequence[i], Sequence[i + 1], i)
        )
        for i in range(len(Sequence) - 1)
    )
