#判断回文
#掌握切片的用法 s[::-1] 这就是从后往前的一个切片
s = input("Please enter a string:")
z = s[::-1]
if s==z:
    print("这是回文字符串")
else:
    print("这不是回文字符串")