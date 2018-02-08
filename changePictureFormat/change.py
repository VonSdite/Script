# -*- coding: utf-8 -*-
# __Author__: Sdite
# __Email__ : a122691411@gmail.com

import os, sys
from PIL import Image

def change(inFile=sys.argv[1], pformat=sys.argv[2]):
    # 可直接通过sys.argv传入图片来操作
    f, e = os.path.splitext(inFile)

    outFile = f + '.' + pformat

    # 判断文件是否已经是目标格式了，这里做的是简单的判断
    if inFile != outFile:
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
    else:
        print('该文件为.{}格式文件'.format(pformat))

if __name__ == '__main__':
    change()

