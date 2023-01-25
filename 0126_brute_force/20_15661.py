
''' https://www.acmicpc.net/problem/15661	링크와 스타트		

            '''

 
from itertools import combinations
 
N = int(input())
 
num = [i for i in range(N)]
arr = [list(map(int, input().split())) for i in range(N) ]
 
MIN = 100000000 
comb_list = list(combinations(num, N//2))
for comb in comb_list:
    start = 0
    link = 0
    remain = [i for i in range(N) if i not in comb]
    for com in combinations(comb, 2):
        start += arr[com[0]][com[1]]
    for ar in combinations(remain, 2):
        link += arr[ar[0]][ar[1]]
    MIN = min(MIN, abs(start - link))
print(MIN)