
''' https://www.acmicpc.net/problem/17626	Four Squares		

'''
from math import sqrt

N = int(input())
sqrt_N = int(sqrt(N))
re = 4
for a in range(1, sqrt_N + 1):
    if a * a == N:
        re = 1
    
    if re == 1:
        break
    for b in range(1, sqrt_N + 1):
        if a * a + b * b  > N:
            break
        if a * a + b * b == N:
            re = 2

        if re <= 2:
            break
        for c in range(1, sqrt_N + 1):
            if a * a + b * b + c * c  > N:
                break
            if a * a + b * b + c * c == N:
                re = 3
                break
print(re)  
