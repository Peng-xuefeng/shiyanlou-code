#考察字符串操作
#要求 从给定的文件中，读取字符串，找出其中的数字，并打印出来
fb = open('E:/learnPythonProject/sample.txt')
s = fb.read()
fb.close()
a = []
for i in s:
    if i.isdigit():
        a.append(i)
numberString = ''.join(a)
print(numberString)