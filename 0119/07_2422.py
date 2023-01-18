''' https://www.acmicpc.net/problem/2422	한윤정이 이탈리아에 가서 아이스크림을 사먹는데		
'''
import itertools

N, M = map(int, input().split())
items = [i for i in range(1, N+1)]
err = [list() for i in range(N+1)]
answer = 0

for i in range(M):
    a, b = map(int, input().split())
    err[min(a, b)].append(max(a,b))
 

for i in range(1, N+1):
    set1 = err[i]
    for j in range(i+1, N+1):
        if j in set1:
            continue
        set2 = set1 + err[j]
        for k in range(j+1, N+1):
            if k in set2:
                continue
            answer += 1

print(answer)


N, M = list(map(int, input().split(" ")))
 
chk = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    t = list(map(int, input().split(" ")))
     
    chk[t[0]][t[1]] = chk[t[1]][t[0]] = 1
cnt = 0
 
for i in range(1, N+1):
    for j in range(i + 1, N+1):
        if chk[i][j]:
            continue
        for k in range(j + 1, N+1):
            if chk[i][k] or chk[j][k]:
                continue
            cnt = cnt + 1
print(cnt)