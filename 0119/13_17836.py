''' https://www.acmicpc.net/problem/17836	공주님을 구해라!
1,1 ->n,m 까지 t 시간 안에 도착
상하좌우 이동 가능
칼 찾으면 벽 통과 

입력
1: n,m,t
2~:  0 :통과  1 :벽  2 :칼

출력
t 시간이내 도착 X : fail출력
             하는 최단 시간 출력
'''
from collections import deque
N,M,T=map(int,input().split())
arr=[ list(map(int,input().split())) for _ in range(N)]
dir=[(1,0),(-1,0),(0,1),(0,-1)]#상하좌우

if N+M-2 >T : #이미 시간초과이므로 Fail
    print('Fail')
    exit(0)

visit=[[0]*M for _ in range(N)]
q=deque()
q.append((0,0))
visit[0][0]=1
answer=10000
while q:
    x,y=q.popleft()
    if x==N-1 and y==M-1:  break #도착 N,M
    if arr[x][y] == 2:
        answer = N-1-x + M-1-y + visit[x][y]-1
    for i in dir:
        nx,ny=x+i[0],y+i[1]
        if 0<=nx<N and 0<=ny<M:
            if visit[nx][ny]==0 and arr[nx][ny]!=1:
                visit[nx][ny]=visit[x][y]+1
                q.append((nx,ny))
if visit[N-1][M-1]>0:
    answer=min(answer,visit[N-1][M-1]-1)
print('Fail' if answer>T else answer)