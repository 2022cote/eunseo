import math

def is_Pal(x):
    x_li = list(str(x))
    x_len=len(x_li) /2   
    
    if  x_len %1 !=0 :  #자릿수 홀수        
        del x_li[x_len]

    x_len = int(x_len)
    for _ in range(x_len):                          
        x2 = x_len-1
        if x_li[x_len] == x_li[x2]:
            x_len+=1            
            x2-=1
        else : return False

   
    return True

def is_prime(x):# 소수 판단 
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


# N보다 크고, 소수이면서  3443 같은 수 구하기


n  = int(input())

while True:
    if str(n) ==str(n)[::-1]:
        if  is_prime(n):         
            print(n) 
            break
    n+=1




