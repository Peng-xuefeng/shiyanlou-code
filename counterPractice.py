#练习Counter的使用
from collections import Counter
c = Counter('ABCCBADDAA')
k =c.most_common(4)
lista = []
for i,j in k:
    lista.append("{}:{},".format(i,j))
print(''.join(lista).rstrip(','))