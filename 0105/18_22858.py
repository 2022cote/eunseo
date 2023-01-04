''' https://www.acmicpc.net/problem/22858	원상 복구 (small)		
'''
n, k = map(int, input().split())
after = list(map(int, input().split()))
D = list(map(int, input().split()))

for _ in range(k):
    tmp = [0]*n
    for i in range(n):
        tmp[D[i]-1] = after[i]
    after = tmp
print(*after)