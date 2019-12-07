#练习os模块
#打印E:\movie下的文件
import os

def view_dir(path):
    """
    练习打印给定目录下的文件
    """
    names = os.listdir(path)
    for name in names:
        print(name)

view_dir('E:/movie')