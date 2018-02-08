# 转化图片格式以及生成缩略图

## 使用方法

1. 先将该项目'changeToJPEG'文件夹路径加入到**环境变量**中(这样更方便使用)

2. 然后就可以如下操作:

**change.py**

*介绍: change.py通过命令行参数一次转化一张图片的格式*

- 命令行输入
```
change.py 图片名.png 所要转化的图片格式
```

- 例:
```
change.py test.png jpg
```


**changes.py**

*介绍: changes.py 通过命令行将当前目录下所有图片转化目标格式，并保存在Res文件夹中*

- 命令行输入
```
changes.py 所要转化的图片格式
```

- 例:
```
changes.py jpg
```

**thumbnail.py**

*介绍: thumbnail.py 通过命令行参数一次生成一张或多张图片的缩略图*

- 命令行输入
```
thumbnail.py 图片名1.png [图片名2.png ...]
```

### BTW
- change.py 属于单张图片处理
- changes.py 可以一次性批量较多的图片
- 当然，最重要的要加入到**环境变量**中！！这样才方便实用
