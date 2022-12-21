
'''
https://www.acmicpc.net/problem/22869 
징검다리 건너기 (small)
'''
n, k = map(int, input().split())
rocks = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
for i in range(n-1): 
    for j in range(i+1, n):
        if (j-i) * (1 + abs(rocks[i]-rocks[j])) <=k  :
            dp[j] =1  
        
if dp[n-1]:
    print('YES')
else:
    print('NO')