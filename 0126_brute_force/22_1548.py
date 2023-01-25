
''' https://www.acmicpc.net/problem/1548	부분 삼각 수열		 

'''

N=int(input())

num=list(map(int,input().split()))
num.sort()

answer=1

for x in range(N-1):
    for z in range(N-1,-1,-1):
            if z<x+1: continue
            if num[x]+num[x+1]>num[z]:    answer=max(z-x+1,answer)



print(answer)