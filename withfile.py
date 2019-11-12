#使用with语句读取文件，它会自动关闭
import os
def read(path):
    if os.path.exists(path):
        with open(path) as fb:
            for line in fb:
                print(line,end="")
    else:
        print("File not exists")

read('E:/learnPythonProject/sample.txt')