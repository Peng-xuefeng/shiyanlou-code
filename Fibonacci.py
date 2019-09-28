#打印斐波那契数列，主要练习while循环，以及python里面一个比较特殊的数据结构 元组
# print中的end参数如何书写
a , b = 0 , 1
while b < 100:
    print(b,end=" ")
    a , b = b , a+b