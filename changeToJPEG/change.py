# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import os, sys
from PIL import Image

def change():    
    PIC_FORMAT = ['.png', '.gif', '.bmp']   # 要转化为JPEG格式的图片格式

    # 当前目录下创建保存结果JPEG的文件夹
    JPEG = 'JPEG/'
    if not os.path.isdir(JPEG):
        os.mkdir(JPEG)

    # 修改当前路径下所有图片为JPEG
    imageSet = os.listdir('.')
    for inFile in imageSet:
        f, e = os.path.splitext(inFile)

        # 判断是否是图片
        if e not in PIC_FORMAT:
            continue        # 不是则continue 

        outFile = JPEG + f + '.jpg'

        try:
            img = Image.open(inFile)
        except FileNotFoundError as e:
            print('找不到 文件 {}'.format(inFile))
            continue
        except:
            print('异常问题 文件 {}'.format(inFile))
            continue

        # png图片有四个通道RGBA, 而JPEG只有三个通道，所以如果是四通道，则只取前三个通道
        if len(img.split()) == 4:
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))

        # 进行格式转化
        try:
            img.save(outFile)
        except IOError as e:
            print("Can't convert {} //".format(inFile), e)
            os.system('del {}'.format(outFile)) # 删除转化错误的文件

if __name__ == '__main__':
    change()

