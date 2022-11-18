'''
2 3 4 5 6 7 8 9 10 11 12 13 14 15
k =1|2     k =2|4      k =3|6  k=4|8 5|10 6|12 7|14  
8|3 9|9 10|15
11|5
12|7
'''
#소수 리스트
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

N_li = [i for i in range(1,N+1)] #1~N 까지 리스트 생성
prime  = GetPrimes(N)#소수 구해주고
Ans_li =  []# 제거 순서대로 list에 넣어줌
i =0#N_li 인덱스 변수
v =2; a =1
while len(Ans_li) < K : #구하는 값: K번째 지워진 수
    if v not in N_li :# 만약 v가 리스트에 없으면 다음 소수로 넘어가기 
        i+=1
        a =1 
    else :              
        if v not in Ans_li: Ans_li.append(v)    #중복없이 하기 위해 v가 제거 리스트에 없을 시 추가
        a+=1 # ex) 2*1 2*2
    v = prime[i]*a #지우는 변수

print(Ans_li[-1])#  K번째 지워진 수 출력