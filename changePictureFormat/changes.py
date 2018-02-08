# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import os, sys
from PIL import Image

def changes(pformat=sys.argv[1]):    
    # 要转化为格式的图片格式
    PIC_FORMAT = ['.jpg', '.png', '.gif', '.bmp', 'tif', 'tiff']   

    # 当前目录下创建保存结果RES的文件夹
    RES = 'Res/'
    if not os.path.isdir(RES):
        os.mkdir(RES)

    # 修改当前路径下所有图片为目标格式
    imageSet = os.listdir('.')
    for inFile in imageSet:
        f, e = os.path.splitext(inFile)

        # 判断是否是图片
        if e not in PIC_FORMAT:
            continue        # 不是则continue 

        outFile = RES + f + '.' + pformat

        try:
            img = Image.open(inFile)
        except FileNotFoundError as e:
            print('找不到 文件 {}'.format(inFile))
            continue
        except:
            print('异常问题 文件 {}'.format(inFile))
            continue

        # png图片有四个通道RGBA, 而RES只有三个通道，所以如果是四通道，则只取前三个通道
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
    changes()

