#최대 공약수
#test case 개수 :t
t = int(input())

def gcd (n1, n2):
    i = 1
    while i <= n2:
        if n1 % i == 0 and n2 %i ==0:
            gcd = i
        i+=1
    return gcd


for _ in range(t): 
    sum=0
    arr = list(map(int , input().split()))
    del arr[0]
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] % arr[i] ==0 : sum+= arr[i]
            else :sum +=gcd(arr[i],arr[j])
    print(sum)
