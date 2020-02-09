from collections.abc import Iterable
from collections.abc import Iterator
print('[] 是否为迭代器： {}'.format(isinstance([],Iterator)))
print('[] 是否为可迭代对象： {}'.format(isinstance([],Iterable)))

print('for y in [1,2,3,4,5]:')
for y in [1,2,3,4,5]:
    print(y)

print('for x in iter([1,2,3,4,5]):')
for x in  iter([1,2,3,4,5]):
    print(x)

print('next():')
it = iter([1,2,3,4,5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a':1,'b':2,'c':3}
print('iter keys:',d)
for k in d.keys():
    print('Keys:',k)

print('iter value:',d)
for v in d.values():
    print('value:',v)

print('iter items:',d)
for k,v in d.items():
    print('items:',k,v)

print('iter enumerate:')
for m,n in enumerate(['A','B','C']):
    print(m,n)

print('iter complex enumerate:')
for p,q in ([(1,2),(3,4),(5,6)]):
    print(p,q)


