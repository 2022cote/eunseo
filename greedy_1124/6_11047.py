#https://www.acmicpc.net/problem/11047
#4790 4 1 2 1 4
# n    1  2  3   4   5          <=10
# 동전 1  5  10  50  100


#입력
n,k = map(int, input().split())

li = [int(input()) for _ in range(n)]#동전 1  5  10  50  100
li.sort(reverse =True)#동전 500  100  50  10 5 1
coin=0
for i in range(n):
     
    coin += k//li[i]
    k =  k% li[i]

print(coin)