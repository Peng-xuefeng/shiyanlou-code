#统计一个任意文本中行，空格，制表符的数量
#本次代码 训练的是sys.argv的使用 如何使用命令行去调用python文件
#注意一些用到的模块 os.path.exists()可以直接判断文件是否存在
import sys
import os
def parse_file(path):
    """
    这段函数用来执行具体的功能，分析文件中的行，空格等
    """
    spaces = 0
    tabs = 0
    fd = open(path)
    for i,line in enumerate(fd):
        spaces +=line.count(' ')
        tabs +=line.count('\t')
    fd.close()
    return (tabs,spaces,i+1)
def main(path):
    """
    这段函数用来调用parse_file
    """
    if os.path.exists(path):
        tabs,spaces,lines = parse_file(path)
        print("Spaces {}. Tabs {}  lines {}".format(spaces,tabs,lines))
        input("Enter:")
        return True
    else:
        return False
if __name__ == "__main__":
    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        sys.exit(1)
    sys.exit(0)
    