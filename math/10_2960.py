'''
2 3 4 5 6 7 8 9 10 11 12 13 14 15
k =1|2     k =2|4      k =3|6  k=4|8 5|10 6|12 7|14  
8|3 9|9 10|15
11|5
12|7
'''
#소수 찾는 프로그램 필요
def GetPrimes(n):
    primeSeeds = []
    if n <11:
        primeSeeds = [2,3,5,7]
    else :
        primeSeeds = GetPrimes(int(n**0.5)+1)
    primes = [1 for _ in range(n)]

    for i in primeSeeds:
        for j in range(2, int(n/i)+1):
            primes[i*j-1] = 0
    result=[]
    for i in range(2, n+1):
        if primes[i-1]==1:
            result.append(i)
    return result


#입력
N,K = map(int , input().split())

N_li = [i for i in range(1,N+1)]
prime  = GetPrimes(N)
Ans_li =  []
i =0#N_li 인덱스 변수
v =2; a =1
while len(Ans_li) < K :    
    if v not in N_li :
        i+=1
        a =1
    else :              
        if v not in Ans_li: Ans_li.append(v)    
        a+=1
    v = prime[i]*a #지우는 변수

print(Ans_li[-1])