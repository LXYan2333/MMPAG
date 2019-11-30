# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
from sys import argv,path
import nbtlib
from nbtlib.tag import *

def d(a,b,c,d,e,f):
    return abs(a-d)+abs(b-e)+abs(c-f)

def sci(g):
    """
    返回最接近目标像素颜色的地图色ID
    Python学得不好，垃圾代码，见谅。"""
    a = g[0]
    b = g[1]
    c = g[2]
    lst=[]
    lst.append(d(a,b,c,127, 178, 56))
    lst.append(d(a,b,c,247, 233, 163))
    lst.append(d(a,b,c,199, 199, 199))
    lst.append(d(a,b,c,255, 0, 0))
    lst.append(d(a,b,c,160, 160, 255))
    lst.append(d(a,b,c,167, 167, 167))
    lst.append(d(a,b,c,0, 124, 0))
    lst.append(d(a,b,c,255, 255, 255))
    lst.append(d(a,b,c,164, 168, 184))
    lst.append(d(a,b,c,151, 109, 77))
    lst.append(d(a,b,c,112, 112, 112))
    lst.append(d(a,b,c,64, 64, 255))
    lst.append(d(a,b,c,143, 119, 72))
    lst.append(d(a,b,c,255, 252, 245))
    lst.append(d(a,b,c,216, 127, 51))
    lst.append(d(a,b,c,178, 76, 216))
    lst.append(d(a,b,c,102, 153, 216))
    lst.append(d(a,b,c,229, 229, 51))
    lst.append(d(a,b,c,127, 204, 25))
    lst.append(d(a,b,c,242, 127, 165))
    lst.append(d(a,b,c,76, 76, 76))
    lst.append(d(a,b,c,153, 153, 153))
    lst.append(d(a,b,c,76, 127, 153))
    lst.append(d(a,b,c,127, 63, 178))
    lst.append(d(a,b,c,51, 76, 178))
    lst.append(d(a,b,c,102, 76, 51))
    lst.append(d(a,b,c,102, 127, 51))
    lst.append(d(a,b,c,153, 51, 51))
    lst.append(d(a,b,c,25, 25, 25))
    lst.append(d(a,b,c,250, 238, 77))
    lst.append(d(a,b,c,92, 219, 213))
    lst.append(d(a,b,c,74, 128, 255))
    lst.append(d(a,b,c,0, 217, 58))
    lst.append(d(a,b,c,129, 86, 49))
    lst.append(d(a,b,c,112, 2, 0))
    lst.append(d(a,b,c,209, 177, 161))
    lst.append(d(a,b,c,159, 82, 36))
    lst.append(d(a,b,c,149, 87, 108))
    lst.append(d(a,b,c,112, 108, 138))
    lst.append(d(a,b,c,186, 133, 36))
    lst.append(d(a,b,c,103, 117, 53))
    lst.append(d(a,b,c,160, 77, 78))
    lst.append(d(a,b,c,57, 41, 35))
    lst.append(d(a,b,c,135, 107, 98))
    lst.append(d(a,b,c,87, 92, 92))
    lst.append(d(a,b,c,122, 73, 88))
    lst.append(d(a,b,c,76, 62, 92))
    lst.append(d(a,b,c,76, 50, 35))
    lst.append(d(a,b,c,76, 82, 42))
    lst.append(d(a,b,c,142, 60, 46))
    lst.append(d(a,b,c,37, 22, 16))
    return lst.index(min(lst))+2

def cid2bid(a):
    '''根据地图色ID返回合适的方块ID
    依据方块资源获取难易程度与是否可再生选择
    也是垃圾代码'''
    x = {1: 'grass_block', 2: 'birch_planks', 3: 'mushroom_stem', 4: 'redstone_block', 5: 'ice', 6: 'iron_block', 7: 'oak_leaves', 8: 'snow_block', 9: 'cobblestone', 10: 'jungle_planks', 11: 'cobblestone', 12: 'water', 13: 'oak_planks', 14: 'diorite', 15: 'acacia_planks', 16: 'magenta_concrete', 17: 'light_blue_concrete', 18: 'yellow_concrete', 19: 'lime_concrete', 20: 'pink_concrete', 21: 'gray_concrete', 22: 'light_gray_concrete', 23: 'cyan_concrete', 24: 'purple_concrete', 25: 'blue_concrete', 26: 'brown_concrete', 27: 'green_concrete', 28: 'red_concrete', 29: 'black_concrete', 30: 'gold_block', 31: 'prismarine_bricks', 32: 'lapis_block', 33: 'emerald_block', 34: 'spruce_planks', 35: 'netherrack', 36: 'white_terracotta', 37: 'orange_terracotta', 38: 'magenta_terracotta', 39: 'light_blue_terracotta', 40: 'yellow_terracotta', 41: 'lime_terracotta', 42: 'pink_terracotta', 43: 'gray_terracotta', 44: 'light_gray_terracotta', 45: 'cyan_terracotta', 46: 'purple_terracotta', 47: 'blue_terracotta', 48: 'brown_terracotta', 49: 'green_terracotta', 50: 'red_terracotta', 51: 'black_terracotta'}
    return x.get(a)


    

path.append('.')

print('您要转换的文件是：',argv[1])
img=Image.open(argv[1])
materiallist = set({})
for i in range(0,img.size[0]):
    for j in range(0,img.size[1]):
        materiallist.add(cid2bid(sci(img.load()[i,j])))
materiallist = tuple(materiallist)
new_file = nbtlib.File({
    '':Compound({
        'DataVersion': Int(1631),
        'size': List[Int]([img.size[0],1,img.size[1]]),
        'palette': List[Compound]([{'Name': String('minecraft:'+str(i))} for i in materiallist]),
        'blocks': List[Compound]([{'pos':List[Int]([j,0,i]),'state':Int(materiallist.index(cid2bid(sci(img.load()[j,i]))))} for i in range(0,img.size[1]) for j in range(0,img.size[0])])
    })},
    gzipped=True
)
new_file.save('picture.nbt')
        
        

