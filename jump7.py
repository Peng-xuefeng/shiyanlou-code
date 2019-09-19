for i in range(1,101):
    k=i-7
    m=i//10
    if i%7==0:
        continue
    elif k%10==0:
        continue
    elif m==7:
        continue
    else:
        print(i)
