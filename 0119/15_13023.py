''' https://www.acmicpc.net/problem/13023	ABCDE

'''

n, m = map(int, input().split())

grap = [[] for _ in range(n)]
friend = [False for _ in range(n)]
result = False

for _ in range(m):
    a, b = map(int, input().split())

    grap[a].append(b)
    grap[b].append(a)


def dfs(s, num):
    global result
    if num == 4:
        result = True
        return

    for i in grap[s]:
        if not friend[i]:
            friend[i] = True
            dfs(i, num+1)
    friend[s] = False
        

for i in range(n):
    friend[i] = True
    dfs(i, 0)
    if result:
        break


if result:
    print(1)

else:
    print(0)