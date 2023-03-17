from itertools import combinations

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

max_s = 0
for a, b, c in combinations(range(m), 3):
    t_sum = 0
    for i in range(n):
        t_sum += max(li[i][a], li[i][b], li[i][c])
    max_s = max(max_s, t_sum)

print(max_s)