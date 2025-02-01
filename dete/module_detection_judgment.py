class ClassJudgment:
    def __init__(self, var):
        self.var = var

    def method_none(self) -> bool:
        '''
        检测是否输入字符串为空
        '''
        return False if self.var == "" else True

    def method_num(self) -> bool:
        '''
        检测输入的字符是否为数字
        '''
        return True if self.var.isnumeric() else False

    def method_notnegative_id(self) -> bool:
        '''
        检测地图画id是否不为负数
        '''
        return True if int(self.var) >= 0 else False

    def method_notnegative_num(self) -> bool:
        '''
        检测地图画遍历数量是否>1
        '''
        return True if int(self.var) > 1 else False


def main() -> None:
    print(ClassJudgment("1").method_num())


if __name__ == "__main__":
    main()
