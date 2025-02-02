import gene.module_var as var


class ClassVarPrefabricate:
    def fuc_inmap(slot_num: int, map_id: int, *args) -> str:
        '''
        生成在箱子里面的地图代码，数值嵌套在地图画代码里面
        :param slot_num: 对应的箱子位置
        :param map_id: 地图id
        :return: 嵌套在地图画代码的字符串
        '''

        local_var = ",%s,%s" % (var.map_Slot.format(
            slot_num), var.map_id.format(map_id))
        return var.map_tag.format(local_var)

    # 在箱子里面的箱子
    def fuc_inbox(slot_num: int, map_num: list[int], data: str, *args) -> str:
        '''
        生成在箱子里面的箱子代码，数值嵌套在箱子代码里面
        :param slot_num: 对应的箱子位置
        :param map_num: 这是一个列表，输入两个值为这个箱子装着的地图画的范围
        :param data: 物品数据
        :return: 嵌套在箱子代码的字符串
        '''

        local_var = ",%s,tag:{%s,%s}" % (var.chest_Slot.format(
            slot_num), var.chest_display.format(map_num[0], map_num[1]), var.chest_BET.format(data))
        return var.chest_tag.format(local_var)

    def fuc_box(map_num: list[int], data: str, *args) -> str:
        '''
        生成在装着整个东西的箱子代码，数值嵌套在箱子代码里面
        :param map_num: 这是一个列表，输入两个值为这个箱子装着的地图画的范围
        :param data: 物品数据
        :return: 整合箱子代码的字符串
        '''

        local_var = ",tag:{%s,%s}" % (var.chest_display.format(
            map_num[0], map_num[1]), var.chest_BET.format(data))
        return var.chest_tag.format(local_var)


def main() -> None:
    print(ClassVarPrefabricate.fuc_box([1, 2], 2))


if __name__ == "__main__":
    main()
