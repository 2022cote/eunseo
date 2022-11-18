#최대 공약수 :GCD

#case 개수 :c
c = int(input())

def gcd (n1, n2): #최대공약수 판단
    i = 1
    while i <= n2:
        if n1 % i == 0 and n2 %i ==0:#둘다 존재하는 수여야 %하면 0이므로
            gcd = i
        i+=1
    return gcd


for _ in range(c): 
    sum=0
    arr = list(map(int , input().split()))
    del arr[0]# arr[0]은 테스트 케이스 수로 필요 X
    arr.sort()# 1. 오름차순으로 정렬해줘서
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] % arr[i] ==0 : sum+= arr[i] #2. n의 배수라면 바로 n 더해줌
            else :sum +=gcd(arr[i],arr[j])# gcd 구해주기
    print(sum)
