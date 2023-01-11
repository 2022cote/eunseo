''' https://www.acmicpc.net/problem/2615	오목	

블로그 참고
''' 
dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]
omok = [list(map(int, input().split())) for _ in range(19)]


def check(x, y, color):
    for i in range(4):
        cnt = 1
        nx, ny = x, y
        for _ in range(4):
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                continue
            if omok[nx][ny] == color:
                cnt += 1

        if cnt == 5:
            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and omok[x - dx[i]][y - dy[i]] == color:
                continue
            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and omok[nx + dx[i]][ny + dy[i]] == color:
                continue
            return [nx, ny]

    return -1


for i in range(19):
    for j in range(19):
        if omok[i][j] != 0:
            res = check(i, j, omok[i][j])
            if res != -1:
                print(1 if omok[i][j] == 1 else 2)
                
                if j == res[1]: # 세로
                    print(i + 1, j + 1)
                elif i == res[0]: # 가로
                    print(i + 1, j + 1)
                elif i < res[0] and j < res[1]: # 왼쪽 대각선 \
                    print(i + 1, j + 1)
                else: # 오른쪽 대각선 /
                    print(res[0] + 1, res[1] + 1)