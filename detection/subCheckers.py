def isNotSpace(Content: tuple[str]) -> bool:
    return not Content[0].isspace()


def isNum(Content: tuple[str]) -> bool:
    return any(Content[0].strip().removeprefix(prefix).isdecimal() for prefix in "+-")


def isNotNegative(Content: tuple[str]) -> bool:
    return isNum(Content) and Content[0].strip()[0] != "-"
