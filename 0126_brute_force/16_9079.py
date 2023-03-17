
''' https://www.acmicpc.net/problem/9079	동전 게임		

 '''
x = int(input())
for i in range(x):
    p = list(map(int, input().split()))
    p.remove(max(p))
    p.remove(min(p))
    if max(p) - min(p) >= 4:
        print('KIN')
    else:
        print(sum(p))