import gene.module_var as var
from gene.module_iteration import func_iteration_num as it


class ClassDisposeNumber:
    def fuc_quantity_finally(num: int, iter: int = 1, *args) -> list[int]:
        '''
        在最后一个箱子里装着的地图画的数量
        :param num: 遍历数量
        :return: 最后一个 箱子里 装的地图画 的数量、该箱子 装着 地图画或箱子 的箱子 的总数量
        '''
        num_finally = 0  # 末位数量
        box_num = 1  # 箱子数量 指的是装地图画的箱子总数量
        while True:
            if num <= var.BOX_CAPACITY ** iter:  # 如果遍历数量小于箱子格数数量
                num_finally = num
                break
            else:  # 如果大于
                num -= var.BOX_CAPACITY ** iter
                box_num += 1

        return [num_finally, box_num]


def main() -> None:
    num = 2
    # 简单的程序
    n = 2
    iter = it(num)-1

    num = ClassDisposeNumber.fuc_quantity_finally(num)

    print(num)


if __name__ == '__main__':
    main()
