from dete.module_detection_judgment import ClassJudgment as dc


def function_detecting_output(id, num):
    id_bool = dc(id)
    num_bool = dc(num)

    if id_bool.method_none() and num_bool.method_none():
        if id_bool.method_num() and num_bool.method_num():
            id = int(id)
            num = int(num)
            if id_bool.method_notnegative_id() and num_bool.method_notnegative_num():
                return True
            else:
                if id_bool.method_notnegative_id():
                    return "地图画编号只接受正整数!"
                elif num_bool.method_notnegative_num():
                    return "遍历数量只接受大于1的正整数!"
        else:
            if id_bool.method_num() == False and num_bool.method_num() == False:
                return "地图画编号和遍历数量只接受正整数!"
            elif id_bool.method_num() == False:
                return "地图画编号只接受正整数!"
            elif num_bool.method_num() == False:
                return "遍历数量只接受大于1的正整数!"
    else:
        if id_bool.method_none() == False and num_bool.method_none() == False:
            return "请输入地图画编号和遍历数量!"
        elif id_bool.method_none() == False:
            return "请输入地图画编号!"
        elif num_bool.method_none() == False:
            return "请输入遍历数量!"


def main() -> None:
    id = "12"
    num = "233"
    print(function_detecting_output(id, num))


if __name__ == "__main__":
    main()
