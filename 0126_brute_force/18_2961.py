
''' https://www.acmicpc.net/problem/2961	도영이가 만든 맛있는 음식		

'''
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(N)] 
com = [combinations(arr, i) for i in range(1, N+1)]
 
answer = 1000000000
for line in com:
    for each in line:
        sour = 1
        bitter = 0
        for e in each:
            sour *= e[0]
            bitter += e[1]

        answer = min(answer, abs(sour - bitter))

print(answer)