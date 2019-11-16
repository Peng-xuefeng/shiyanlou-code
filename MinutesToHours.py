#实现一个函数，将用户输入的分钟数转化为小时数和分钟数，要求小时数尽量大，结果以 XX H , XX M表示
#不得使用input()
#要求用户通过命令行传递分钟数
#例如 程序执行为python3 MinutesToHours.py 80 传入的80就是分钟数 输出为 1 H , 20 M
#如果用户输入的是一个负值，需要使用raise ValueError来抛出异常
#Hours函数调用的时候，需要使用try..except来处理异常，获取异常后需要在屏幕上打出来Parameter Error的错误信息
import sys
def Hours(minutes):
    try:
        if minutes < 0:
            raise ValueError("Value Error!")
        elif minutes >=0 and minutes < 60:
            print("0 H, {} M".format(minutes))
            input("输入回车关闭") 
        else:
            hours = minutes // 60
            new_minutes = minutes - (hours * 60)
            print("{} H , {} M".format(hours,new_minutes))
            input("输入回车关闭")
    except:
        print('Parameter Error')
        input("输入回车关闭") 

def main():
    if __name__ == '__main__':
        try:
            minutes = int(sys.argv[1])
            Hours(minutes)
        except:
            print("Parameter should be number")
            input("Enter something to close")
main()
