''' https://www.acmicpc.net/problem/17836	공주님을 구해라!

'''

N,M,T=map(int,input().split())
arr=[]
dirs=[(1,0),(0,1),(-1,0),(0,-1)]
for _ in range(N):
    arr.append(list(map(int,input().split())))
visit=[[0]*M for _ in range(N)]
q=deque()
q.append((0,0))
visit[0][0]=1
answer=sys.maxsize
while q:
    r,c=q.popleft()
    if r==N-1 and c==M-1:
        break
    if arr[r][c] == 2:
        answer = visit[r][c] + abs(N - r - 1) + abs(M - c - 1)-1
    for i in range(4):
        nr,nc=r+dirs[i][0],c+dirs[i][1]
        if 0<=nr<N and 0<=nc<M:
            if visit[nr][nc]==0 and arr[nr][nc]!=1:
                visit[nr][nc]=visit[r][c]+1
                q.append((nr,nc))
if visit[N-1][M-1]>0:
    answer=min(answer,visit[N-1][M-1]-1)
if answer>T:
    print('Fail')
else:
    print(answer)