from detection.main import function_detecting_output as dom
from generation.main import func_numerical_check as nch

import pyperclip

map_id = input("输入第一张地图画的编号:\n")
map_num = input("输入需遍历的地图画数量:\n")

# 检测输入是否出错
detection_results = dom(map_id, map_num)

if detection_results:
    map_id = int(map_id)
    map_num = int(map_num)

    # 主程序部分(这部分写了我半个月!其中有90%的时间在找bug T^T)
    pyperclip.copy(nch(map_num, map_id))
else:
    print(detection_results)
