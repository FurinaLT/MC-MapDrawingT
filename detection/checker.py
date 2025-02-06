"""
定义检查器，
用预定义与自定义的子检查器传参初始化，
调用检查函数，
返回特定结果。
"""

from collections.abc import Callable
from typing import Self

type Checker_t = Callable[[tuple], bool]


class Checker:
    """
    检查器
    """

    results = {}

    def __init__(self, SubCheckers: dict[Checker_t, str]) -> None:
        """
        初始化
        :param SubCheckers: 子检查器字典, 绑定错误信息
        """
        self.subCheckers = SubCheckers

    def execTask(self, Content: tuple) -> Self:
        """
        调用检查函数
        :param Content: 待检查内容
        """
        for func in self.subCheckers.keys():
            self.results[func] = func(Content)
        return self

    def getResults(self) -> dict[Checker_t, bool]:
        """
        获取结果(bool 返回值)
        :return: 检查函数绑定返回值的字典
        """
        return self.results

    def __bool__(self) -> bool:
        return all(self.results.values())

    def __str__(self) -> str:
        tmp = []
        for func, result in self.results.items():
            if not result:
                tmp.append(self.subCheckers[func])
        return ";".join(tmp)


class CheckerNoMsg(Checker):
    """
    继承 Checker, 不传检查信息
    """

    def __init__(self, SubCheckers: tuple[Checker_t, ...]) -> None:
        """
        初始化
        :param SubCheckers: 仅包含子检查器的元组
        """
        super().__init__(SubCheckers={SubChecker: "" for SubChecker in SubCheckers})
