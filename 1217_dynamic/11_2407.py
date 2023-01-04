import itertools

n,m = map(int,input().split())
n_li = [ i for i in range(n,n-m,-1)]
tot=1
div=1
for i in range(m,0,-1):
    tot *=n_li[i-1]
    div*=i

print(tot//div)    