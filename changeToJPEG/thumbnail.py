# -*- coding: utf-8 -*-
# @Author   : Sdite
# @DateTime : 2018-02-04 12:55:37

import sys
import os
from PIL import Image

def changeToThumbnail(imageSet=sys.argv[1:]):
    SIZE = (128, 128)
    for inFile in imageSet:
        outFile = os.path.splitext(inFile)[0] + '_thumbnail.jpg'
        if inFile != outFile:
            try:
                im = Image.open(inFile)
                im.thumbnail(SIZE)
                im.save(outFile, "JPEG")
            except IOError as e:
                print("Can't create thumbnail for {}".format(inFile))
            except FileNotFoundError as e:
                print("Can't find file {}".format(inFile))
            except:
                print("Error! {}".format(inFile))

if __name__ == '__main__':
    changeToThumbnail()