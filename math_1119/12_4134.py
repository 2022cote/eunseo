
import math

def is_prime(x):# 소수 판단 
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

# test case 개수
tc = int(input())

for t in range(tc):    
    n = int(input()) #입력
    while True: # n과 같거나 커야 하므로
        if is_prime(n): 
            print(n)
            break
        else : n+=1 #해당 x 면 1번 더