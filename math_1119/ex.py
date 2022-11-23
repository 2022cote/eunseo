n =31
for i in range(n,):
    a=b=tar=(int(input()))
    while (a>0) and (b>0):
        a1 = a%10
        b1 = b//10
        if (a%10)==(b//10):
            a=a//10
            b=b//10
            continue
        else:
            break
        print(i)
        break