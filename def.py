#练习函数的定义
def palindrome(s):
    z=s[::-1]
    return z==s
s=input("Please Enter a string:")
if palindrome(s):
    print("是回文")
else:
    print("不是回文")