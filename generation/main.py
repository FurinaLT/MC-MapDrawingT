from gene.module_generate_var import ClassVarPrefabricate as gvar  # 导入最终处理生成模块
from gene.module_iteration import func_iteration_num as ite  # 导入迭代模块
from gene.module_quantity_finally import ClassDisposeNumber as CDN  # 导入计算最后数量模块
import gene.module_var as var

import pyperclip


class ClassBoxHandling:
    def __init__(self, first_box: int, last_map_num: int, map_id: int, func, iter: int = 1, *args) -> None:
        '''
        :param first_box: 所在箱子的箱子数量
        :param last_map_num: 所在箱子的最后一个箱子装的地图画数量
        :param map_id: 初始地图画id
        :param func: 用于生成什么什么字符的东西 参数必须是两个
        :param iter: 地图画迭代器
        '''
        self.first_box = first_box  # 1
        self.last_map_num = last_map_num  # 2
        self.map_id = map_id  # 1234
        self.func = func
        self.iter = iter  # 1

    def __str__(self) -> str:
        text = ''
        for i in range(self.first_box):
            if i + 1 < self.first_box:
                text += ("" if i == 0 else ",") + gvar.fuc_inbox(
                    i, [self.map_id, self.map_id + (var.BOX_CAPACITY ** self.iter) - 1], self.func((var.BOX_CAPACITY ** self.iter), self.map_id, self.iter))
            else:
                text += ("" if i == 0 else ",") + gvar.fuc_inbox(
                    i, [self.map_id, self.map_id + self.last_map_num - 1], self.func(self.last_map_num, self.map_id, self.iter))
            self.map_id += var.BOX_CAPACITY ** self.iter
        return text


class ClassBasicTreatment:
    def map(map_num: int, map_id: int, *args) -> str:
        '''
        :param map_num: 地图画遍历数量
        :param map_id: 初始地图画id
        '''
        text = ''

        for i in range(map_num):
            text += ("" if i == 0 else ",") + gvar.fuc_inmap(i, map_id + i)

        return text

    def box(map_num: int, map_id: int, *args) -> str:
        '''
        :param map_num: 地图画遍历数量
        :param map_id: 初始地图画id
        '''
        return ClassBoxHandling(first_box=CDN.fuc_quantity_finally(map_num)[1], last_map_num=CDN.fuc_quantity_finally(map_num)[0], map_id=map_id, func=ClassBasicTreatment.map)

    def ilbox(map_num: int, map_id: int, iter: int = 1, *args):
        '''
        :param map_num: 地图画遍历数量
        :param map_id: 初始地图画id
        :param iter: 地图画迭代器(默认为1)
        '''
        iter -= 1

        if iter > 1:  # 如果未到最后一个
            return ClassBoxHandling(first_box=CDN.fuc_quantity_finally(map_num, iter)[1], last_map_num=CDN.fuc_quantity_finally(map_num, iter)[0], map_id=map_id, func=ClassBasicTreatment.ilbox, iter=iter)
        elif iter <= 1:  # 最后一个!
            return ClassBasicTreatment.box(map_num, map_id)


def func_numerical_check(map_num: int, map_id: int) -> str:

    if ite(map_num) == 1:
        return gvar.fuc_box([map_id, map_id+map_num-1], ClassBasicTreatment.map(map_num, map_id))
    elif ite(map_num) == 2:
        return gvar.fuc_box([map_id, map_id+map_num-1], ClassBasicTreatment.box(map_num, map_id))
    elif ite(map_num) >= 3:
        return gvar.fuc_box([map_id, map_id+map_num-1], ClassBasicTreatment.ilbox(map_num, map_id, ite(map_num)))


def main() -> None:
    pyperclip.copy(func_numerical_check(729+1, 1234))


if __name__ == '__main__':
    main()
