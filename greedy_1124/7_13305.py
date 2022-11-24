#https://www.acmicpc.net/problem/13305
#도로의 길이   2   3   1  -> 6L 필요
#리터당 가격 5---2---4---1


n = int(input())
li = list(map(int, input().split()))
cost = list(map(int, input().split()))


tot =0

for i in range(n-1):# 5 2 4
    if i ==0:  c=cost[i]
    if c > cost[i]: c = cost[i]    
    tot += c * li[i]

print(tot)
