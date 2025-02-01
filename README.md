# 简介

一个基于IBE MOD遍历我的世界地图画的一个小工具，输出SNBT数据或原版命令

# 食用方法

_之后的食用方法会在项目完成后做_

现在进度：UI部分编写

# 废话

<h4 style="text-align:center;">启发</h4>

这是一个地图画，在IBE里他的物品数据是这样的(在SNBT编辑器里):

```
{Count:1b,id:"minecraft:filled_map",tag:{map:地图画编号}}
```

以这样的方式填上地图画编号后可以直接获取到对应该编号的地图画

如果需要多个地图画编号连续的地图画
获取方式则非常麻烦

例如我需要一个地图画编号从1~9的地图画
那么我需要以这样的方式一个个地获取:

```
{Count:1b,id:"minecraft:filled_map",tag:{map:1}}
{Count:1b,id:"minecraft:filled_map",tag:{map:2}}
{Count:1b,id:"minecraft:filled_map",tag:{map:3}}
{Count:1b,id:"minecraft:filled_map",tag:{map:4}}
{Count:1b,id:"minecraft:filled_map",tag:{map:5}}
{Count:1b,id:"minecraft:filled_map",tag:{map:6}}
{Count:1b,id:"minecraft:filled_map",tag:{map:7}}
{Count:1b,id:"minecraft:filled_map",tag:{map:8}}
{Count:1b,id:"minecraft:filled_map",tag:{map:9}}
```

非常的麻烦，也非常的不必要

<h4 style="text-align:center;">思路</h4>

用一个箱子多个箱子来装这些地图画，如果多出来就用连续嵌套箱子的方法

这是一个装有草方块的箱子的在IBE SNBT编辑器里物品数据:

```
{Count:1b,id:"minecraft:chest",tag:{BlockEntityTag:{Items:[{Count:1b,Slot:0b,id:"minecraft:grass_block"}],id:"minecraft:chest"}}}
```

我们把它拆开来看，就是这样的:

- 箱子:`{Count:1b,id:"minecraft:chest"}`
- 物品数据:`tag:{}`
- 方块实体数据:`BlockEntityTag:{}`
- 物品列表:`Items:[]`

这样就很容易理解了，在物品列表里，可以放入很多个物品，而这些物品不能直接放入
要在里面加入一个标签:`Slot`，后面跟着在当前箱子里的位置



