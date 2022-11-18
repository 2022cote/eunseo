import math 
n = int(input())

arr = list(map(int, input().split()))

#arr = 4 2 8 5 7 k =4 서로수 (5+7)/2 ->6
k = int(input())

sum=0
div = 0
#  변수 1개 서로수 구해주고 리스트화 한 뒤 나눠주기
for i in arr:
    a = math.gcd(i,k)
    if a == 1: 
        sum +=i
        div +=1
    else : pass
print(sum/div)