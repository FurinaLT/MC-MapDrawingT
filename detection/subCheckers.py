"""
预定义子检查器
"""


def isNotSpace(Content: tuple[str]) -> bool:
    """
    判断是否为空串
    包装 str.isspace()
    :param Content: 待检查内容
    :return: 若不是空串则返回真
    """
    return not Content[0].isspace()


def isNum(Content: tuple[str]) -> bool:
    """
    判断字符串内容是否为十进制整数
    包装 str.isdecimal(), 允许前后空字符和一位符号前缀(+/-)
    :param Content: 待检查内容
    :return: 若是十进制整数则返回真
    """
    return any(Content[0].strip().removeprefix(prefix).isdecimal() for prefix in "+-")


def isNotNegative(Content: tuple[str]) -> bool:
    """
    判断十进制整数是否为非负数
    调用 .isNum 判断十进制整数
    :param Content: 待检查内容
    :return: 若是十进制非负整数则返回真
    """
    return isNum(Content) and Content[0].strip()[0] != "-"
