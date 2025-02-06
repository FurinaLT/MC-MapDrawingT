"""
main
"""

import pyperclip
from detection.checker import CheckerNoMsg as Checker
from detection.subCheckers import isNotSpace, isNum, isNotNegative
from generation.constructor import Constructor

mapId = input("输入第一张地图画的编号:\n")
mapNum = input("输入需遍历的地图画数量:\n")

# 检测输入是否出错
chkr = Checker((isNotSpace, isNum, isNotNegative))
templateErrMsg = {
    isNotSpace: "{Str}不能为空!",
    isNum: "{Str}应为数字!",
    isNotNegative: "{Str}应为正数!",
}
flagPass = True
for name, value in {"初始地图ID": mapId, "地图数量": mapNum}.items():
    for func, result in chkr.execTask((value,)).getResults().items():
        if not result:
            print(templateErrMsg[func].format(Str=name))
            flagPass = False

if flagPass:
    # 主程序部分(这部分写了我半个月!其中有90%的时间在找bug T^T)
    strBox = str(Constructor(int(mapId), int(mapId) + int(mapNum)))
    print(strBox)
    try:
        pyperclip.copy(strBox)
    except pyperclip.PyperclipException as exception:
        print(f"复制失败!\n请手动复制到剪贴板\n以下是pyperclip原始报错信息:\n{exception}")
    else:
        print("已复制到剪贴板!")
