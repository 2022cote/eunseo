
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
res = [0] * (n + 1)

for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

def dfs(v):
    visited[v] = 1
    
    for i in graph[v]:
        if visited[i] == 0:
            res[i] = v
            dfs(i)
            
dfs(1)
for i in range(2, n+1):
    print(res[i])