'''
https://www.acmicpc.net/problem/1890
점프
'''
import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if lst[i][j] == 0:
            continue
        jump = lst[j][i]
        
        if j+jump < n:
            dp[j+jump][i] += dp[j][i]
        if i+jump < n:
            dp[j][i+jump] += dp[j][i]

print(dp[-1][-1])