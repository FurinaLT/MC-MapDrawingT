import gene.module_var as var  # 每个箱子里装着的地图画数量


def func_iteration_num(num: int) -> int:
    '''
    返回迭代值
    :param num: 遍历数量
    :return: 迭代次数
    '''

    local_var_iteration_num = 1  # 迭代次数

    while True:
        if num <= var.BOX_CAPACITY ** local_var_iteration_num:
            break
        else:
            local_var_iteration_num += 1

    return local_var_iteration_num


def main() -> None:
    print(f"迭代次数: {func_iteration_num(28)}")


if __name__ == "__main__":
    main()
