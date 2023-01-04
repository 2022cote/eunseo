''' https://www.acmicpc.net/problem/21608	상어 초등학교		  '''
N = int(input())
total = 0
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]
stu = []
feel = [[0 for i in range(N)] for j in range(N)]
arr = [[0 for i in range(N)] for j in range(N)]
save = [[] for i in range(N**2+1)]
for i in range(N**2):
    a = list(map(int, input().split()))
    stu.append(a)
    save[a[0]].append(a[1:])
for i in range(N**2):
    temp = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] != 0:
                continue
            like = 0
            empty = 0
            for z in range(4):
                dx = x + nx[z]
                dy = y + ny[z]
                if dx < 0 or dx >= N or dy < 0 or dy >= N:
                    continue
                if  arr[dx][dy] in stu[i][1:]:
                    like += 1
                if arr[dx][dy] == 0:
                    empty += 1
            temp.append((like, empty, (x,y)))
    temp.sort(key = lambda x : (-x[0], -x[1], x[2]))
    arr[temp[0][2][0]][temp[0][2][1]] = stu[i][0]
