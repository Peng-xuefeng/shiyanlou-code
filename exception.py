#学习try..except
def get_num():
    floatnumber = float(input("Please Enter a number:"))
    return floatnumber
try:
    print(get_num())
except:
    print("Error")
else:
    print("没有发生异常")
finally:
    print("不知道发生异常没，反正我最后都会执行")