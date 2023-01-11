''' https://www.acmicpc.net/problem/16926	배열 돌리기 1		
'''
N = int(input())
r = [0 for _ in range(365 + 1)]
for _ in range(N):
    S, E = map(int, input().split(' '))
    for i in range(S, E + 1):
        r[i] += 1
r.append(0)        
ans,m ,l = 0,0,0

for h in r:
    if h == 0:
        ans += l * m
        m, l = 0, 0
 
    m = m(m, h)
    l += 1
print(ans)