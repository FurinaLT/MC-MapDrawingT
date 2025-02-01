# 箱子总容量
BOX_CAPACITY = 27  # 箱子容量

# 箱子外套标签+tag
chest_tag = '{{Count:1b,id:"minecraft:chest"{}}}'  # 外壳  # 封口

# 箱子-display属性
chest_display = 'display:{{Name:\'{{"italic":false,"extra":[{{"text":""}},{{"color":"dark_gray","text":"["}},{{"color":"dark_aqua","text":"{}"}},{{"color":"gray","text":"~"}},{{"color":"aqua","text":"{}"}},{{"color":"dark_gray","text":"]"}}],"text":""}}\'}}'

# 箱子-BlockEntityTag属性
chest_BET = 'BlockEntityTag:{{Items:[{}],id:"minecraft:chest"}}'

# 箱子-Slot属性
chest_Slot = "Slot:{}b"

# 地图外壳
map_tag = '{{Count:1b,id:"minecraft:filled_map"{}}}'

# 地图-Slot属性
map_Slot = "Slot:{}b"

# 地图-map属性+tag
map_id = "tag:{{map:{}}}"


def main() -> None:
    print(chest_tag.format(f",{chest_display.format(1, 2)}"))


if __name__ == "__main__":
    main()
