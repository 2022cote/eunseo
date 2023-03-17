
''' https://www.acmicpc.net/problem/2503	숫자 야구		

            '''
 
 
from itertools import permutations

num = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))  # 서로 다른 수의 세 자리 숫자

t = int(input())
for _ in range(t):
    q, str, ball = map(int, input().split())
    re  = 0   
    for i in range(len(num)):
        sCn, bCn = 0, 0
        i -= re 
        for j in range(3):
            q[j] = int(q[j])
            if q[j] in num[i]: 
                if j == num[i].index(q[j]): sCn += 1
                else: bCn += 1
        if sCn != str or bCn != ball:   
            num.remove(num[i])   
            re += 1   
print(len(num))  




 