#练习while循环以及一些格式的表示 比如{:5d} {:7.3f}代表什么意思要明白,python里可以有()哦
F = 0
while F <= 250:
    celsius = (F - 32) / 1.8
    print('{:5d} {:7.3f}'.format(F,celsius))
    F += 25
