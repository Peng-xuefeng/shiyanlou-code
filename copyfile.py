#练习文件拷贝
#先读出来，再写进入
f1 = open('E:/learnPythonProject/sample.txt')
s = f1.read()
f1.close()
print("源端文件的内容是： %s" %s)
f2 = open('E:/learnPythonProject/sample2.txt','w')
f2.write(s)
f2.close()
f2 = open('E:/learnPythonProject/sample2.txt')
t = f2.read()
print("目的端文件的内容是： %s" %t)