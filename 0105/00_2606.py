n = int(input())
m = int(input())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
cnt = 0
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
 
def dfs(graph, visited, v):
    cn =0
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, visited, i)
    return cnt 

print(dfs(graph,visited,1))