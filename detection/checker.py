from collections.abc import Callable
from typing import Self

type Checker_t = Callable[[tuple], bool]


class Checker:
    results = dict()

    def __init__(self, SubCheckers: dict[Checker_t, str]) -> None:
        self.subCheckers = SubCheckers

    def execTask(self, Content: tuple) -> Self:
        for func in self.subCheckers.keys():
            self.results[func] = func(Content)
        return self

    def getResults(self) -> dict[Checker_t, bool]:
        return self.results

    def __bool__(self) -> bool:
        return all(self.results.values())

    def __str__(self) -> str:
        tmp = list()
        for func, result in self.results.items():
            if not result:
                tmp.append(self.subCheckers[func])
        return ";".join(tmp)


class CheckerNoMsg(Checker):
    def __init__(self, SubCheckers: tuple[Checker_t, ...]) -> None:
        self.subCheckers = {SubChecker: "" for SubChecker in SubCheckers}
