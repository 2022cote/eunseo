''' https://www.acmicpc.net/problem/1244	    스위치 켜고 끄기		'''
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def num_bumbs(x, y):
    cnt = 0
    for i in range(8):
        tx = x+dx[i]
        ty = y+dy[i]
        if 0<=tx<N and 0<=ty<N:
            if bumb[tx][ty] == '*':
                cnt += 1
    arr[x][y] = str(cnt)

N = int(input())
bumb = [list(input()) for _ in range(N)]
arr = [list(input()) for _ in range(N)]
for i in range(8):
    for j in range(8):
        if arr[i][j] == 'x':
            num_bumbs(i, j)
for i in range(8):
    print(''.join(arr[i]))