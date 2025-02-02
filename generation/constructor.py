class Map:
    Template = '{{Count:1b,Slot:{Slot}b,id:"minecraft:filled_map",tag:{{map:{MapId}}}}}'

    def __init__(self, Slot: int, MapId: int):
        self.Slot = Slot
        self.MapId = MapId

    def __str__(self) -> str:
        return self.Template.format(Slot=self.Slot, MapId=self.MapId)

    def __format__(self) -> str:
        return self.__str__()


class Box:
    Template = '{{Count:1b,{Slot}id:"minecraft:chest",tag:{{BlockEntityTag:{{Items:{Items},id:"minecraft:chest"}},display:{{Name:\'{{"Italic":false,"Extra":[{{"text":""}},{{"color":"dark_gray","text":"["}},{{"color":"dark_aqua","text":"{Begin}"}},{{"color":"gray","text":","}},{{"color":"aqua","text":"{End}"}},{{"color":"dark_gray","text":")"}}],"text":""}}\'}}}}}}'

    def __init__(self, Begin: int, End: int, Slot: int = -1):
        from .iterator import Iterator

        self.Begin = Begin
        self.End = End
        self.Items = Iterator(Begin, End)
        self.Slot = Slot

    def __str__(self) -> str:
        return self.Template.format(
            Slot=f"Slot:{self.Slot}b," if self.Slot != -1 else "",
            Begin=self.Begin,
            End=self.End,
            Items=f"[{','.join(map(str, self.Items))}]",
        )

    def __format__(self) -> str:
        return self.__str__()


class Constructor(Box):
    pass
