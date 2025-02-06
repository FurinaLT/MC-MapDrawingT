# pylint: disable = C0301, R0903
"""
定义地图与箱子的简单构造对象和构造器
"""


class Map:
    """
    简单地图构造对象
    """

    TEMPLATE = '{{Count:1b,Slot:{Slot}b,id:"minecraft:filled_map",tag:{{map:{MapId}}}}}'

    def __init__(self, Slot: int, MapId: int) -> None:
        self.slot = Slot
        self.mapId = MapId

    def __str__(self) -> str:
        return self.TEMPLATE.format(Slot=self.slot, MapId=self.mapId)


class Box:
    """
    简单箱子构造对象
    """

    TEMPLATE = '{{Count:1b,{Slot}id:"minecraft:chest",tag:{{BlockEntityTag:{{Items:{Items},id:"minecraft:chest"}},display:{{Name:\'{{"Italic":false,"Extra":[{{"text":""}},{{"color":"dark_gray","text":"["}},{{"color":"dark_aqua","text":"{Begin}"}},{{"color":"gray","text":","}},{{"color":"aqua","text":"{End}"}},{{"color":"dark_gray","text":")"}}],"text":""}}\'}}}}}}'

    def __init__(self, Begin: int, End: int, Slot: int = -1) -> None:
        from .iterator import iterator

        self.begin = Begin
        self.end = End
        self.items = iterator(Begin, End)
        self.slot = Slot

    def __str__(self) -> str:
        return self.TEMPLATE.format(
            Slot=f"Slot:{self.slot}b," if self.slot != -1 else "",
            Begin=self.begin,
            End=self.end,
            Items=f"[{','.join(str(i) for i in self.items)}]",
        )


class Constructor(Box):
    """
    构造器
    继承自 Box
    完全等同
    """
