#100以内的数字，逢7跳过，7的倍数以及数字中含有7的都跳过
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
