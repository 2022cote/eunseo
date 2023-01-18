
''' https://www.acmicpc.net/problem/2668	숫자고르기		

'''

N = int(input())
graph = [0]


def dfs(x):
    global result
    visit[x] = True
    cycle.append(x)
    n = graph[x]
    if visit[n]:
        if n in cycle:
            result += cycle[cycle.index(n):]
    else:
        dfs(n)


visit = [True]+[False]*N
for _ in range(1, N+1):
    t = int(input())
    graph.append(t)

result = []
for i in range(1, N+1):
    if not visit[i]:
        cycle = list()
        dfs(i)
result.sort()
print(len(result))
for i in result:
    print(i)
