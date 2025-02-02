from . import PASS


class Checker:
    def isNull(self) -> str:
        return PASS if self.Content != "" else "字符串不能为空"

    SubChecker = {"isNull": isNull}
    EnabledChecker = ["isNull"]
    Result = dict()

    def __init__(self, Content: str, EnabledChecker: list[str] = EnabledChecker):
        self.Content = Content
        self.EnabledChecker = EnabledChecker
        for Sub in self.EnabledChecker:
            self.Result[Sub] = self.SubChecker[Sub](self)

    def __bool__(self) -> bool:
        return all(map(lambda i: i == PASS, self.Result.values()))

    def __str__(self) -> str:
        Temp = list()
        for S in self.Result.values():
            if S != PASS:
                Temp.append(S)
        return ";".join(Temp)
