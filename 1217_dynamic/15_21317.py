''' 
 1.  현 위치에서 다음 돌로 이동
 2. 1개의 돌을 건너뛰어 이동
 3. 2개의 돌을 건너뛰어 이동 - k 에너지 
 '''

def dfs(node, E , key):
    li=[]
    global min_E
    if E >= min_E:
        return
    if node == N:
        min_E = min(min_E, E)
        return
    #1번
    if node + 1 <= N: dfs(node + 1, E + dp[node][0], key)# 101 -> 2,2,1
    #2번
    if node + 2 <= N: dfs(node + 2, E + dp[node][1], key)
    #3번
    if node + 3 <= N and key:  dfs(node + 3, E + K, 0)


N = int(input())
dp =[[0,0]] 
for i in range(1,N): dp.append(list(map(int,input().split())) )
    
K = int(input())
min_E = float('inf')
dfs(1, 0, 1)#노드 1개 E =0 
print(min_E)