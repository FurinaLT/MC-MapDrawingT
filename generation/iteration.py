from .struct import Box, Map


def func_iteration_num(num: int) -> int:
    """
    返回迭代值
    :param num: 遍历数量
    :return: 迭代次数
    """

    local_var_iteration_num = 1  # 迭代次数

    while True:
        if num <= var.BOX_CAPACITY**local_var_iteration_num:
            break
        else:
            local_var_iteration_num += 1

    return local_var_iteration_num


def Iterator(Begin: int, End: int) -> list[Map | Box]:
    from math import ceil, log

    Step = 27 ** ceil(log(End - Begin, 27) - 1) if End - Begin > 1 else 1

    Sequence = list(range(Begin, End, Step)) + [End]
    return list(
        (
            Map(i, Sequence[i])
            if Sequence[i + 1] - Sequence[i] == 1
            else Box(Sequence[i], Sequence[i + 1], i)
        )
        for i in range(len(Sequence) - 1)
    )
