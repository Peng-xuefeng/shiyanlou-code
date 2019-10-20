#计算矩阵的哈达玛积
#矩阵为n x n 
# 利用嵌套列表存储矩阵[[1,2],[3,4]]
# 矩阵的每一行就是一个列表，将这个列表作为元素添加到大列表
# a.append(int(x) for x in input().split())
n = int(input("Enter the value of n:"))
a = []
print("Enter the value of Matrix A:")
for i in range(n):
    a.append([int(x) for x in input().split()])
b = []
print("Enter the value of Matrix B:")
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After the Matrix multiplication:")
print("*" * 7)
for x in c:
    for y in x:
        print(y,end=" ")
    print()
print("*" * 7)
