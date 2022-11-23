#https://www.acmicpc.net/problem/20115

n = int(input())
drink = list(map(int, input().split()))
drink.sort(reverse =True)
sum =drink[0]
del drink[0]
for i in drink :
    sum+= i/2
print(sum)