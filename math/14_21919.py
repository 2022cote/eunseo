'''5\n  2 3 5 6 8 소수 2 3 5 -> print( 2*3*5)
if 소수 X  print(-1)
'''
import math
def is_prime(x):# 소수 판단 
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


n = int(input())

n_li = set(map(int, input().split())) #set을 사용해서 중복 제거

sum =0
for i in n_li:    
    if is_prime(i):  #소수이면 곱해주기
        if sum ==0 : sum = i
        else : sum *=i
if sum == 0:sum =-1#sum이 0이면 모두 소수X으로 -1출력
    
print(sum)
