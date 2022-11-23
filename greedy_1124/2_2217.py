#https://www.acmicpc.net/problem/2217
#k개의 로프 | 중량 w | 각각의 로프:  w/k 만큼의 중량

#입력
n = int(input())

a = [ int(input()) for _ in range(n)] #a리스트에 넣고
a.sort(reverse=True)#큰수부터 정리

# 중량은 작은수 *i+1
li = [a[i]*(i+1) for i in range(n) ]#큰수부터 가능한 
li.sort() #작은 수 부터 정렬
print(li[-1])
'''
li = copy.deepcopy(a)
for i in range(2,n):
    nCr = list(itertools.combinations(a, i))
    li = li +nCr
max =0
'''
    
