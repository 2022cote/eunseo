
''' https://www.acmicpc.net/problem/20207	달력

'''

n, m, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

nm= min(n, m)//2
for i in range(nm):
    arr = [A[i][j] for j in range(i, m-i-1)] + \
            [A[j][m-i-1] for j in range(i, n-i-1)] + \
            [A[n-i-1][j] for j in range(m-i-1, i, -1)] + \
            [A[j][i] for j in range(n-i-1, i, -1)]
    r = r%len(arr)
    arr = arr[r:] + arr[:r]
    idx = 0
    for j in range(i, m-i-1):
        A[i][j] = arr[idx]
        idx += 1
    for j in range(i, n-i-1):
        A[j][m-i-1] = arr[idx]
        idx += 1
    for j in range(m-i-1, i, -1):
        A[n-i-1][j] = arr[idx]
        idx += 1
    for j in range(n-i-1, i, -1):
        A[j][i] = arr[idx]
        idx += 1

for a in A:
    print(*a)