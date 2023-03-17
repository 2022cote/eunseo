

''' https://www.acmicpc.net/problem/14620	꽃길		

'''
from itertools import combinations
 
N = int(input())
arr = [list(map(int, input().split())) for i in range(N) ]
flower = []
MIN = 100000000
nx = [-1, 0, 1, 0]
ny = [0, -1, 0, 1]


for i in range(1, N-1):
    for j in range(1, N-1):
        flower.append((i,j))
for flower_comb in combinations(flower, 3):
    temp = 0
    flag = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for flo in flower_comb:
        if visited[flo[0]][flo[1]] == 0:
            visited[flo[0]][flo[1]]
            temp += arr[flo[0]][flo[1]]
        else:
            flag = 1
            break
        for i in range(4):
            dx = flo[0] + nx[i]
            dy = flo[1] + ny[i]
            if visited[dx][dy] == 0:
                visited[dx][dy] = 1
                temp += arr[dx][dy]
            else:
                flag = 1
                break
    if not flag:
        MIN = min(MIN, temp)
print(MIN)