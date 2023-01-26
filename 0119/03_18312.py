''' https://www.acmicpc.net/problem/18312	시각
첫째 줄에 정수 N과 K
00시 00분 00초부터 N시 59분 59초까지 모든 시각 중 K 포함되는 시간 모두 구하기
k=2
1002
2011
'''
n,k = map(str ,input().split())
li = [['0',str(i)] for i in range(10)]

# h = 시
if len(n)==2 : h = li +[list(str(i)) for i in range(10,int(n)+1)]
else : h = li[:int(n)+1]

m = li +[list(str(i)) for i in range(10,60)]#분
s = m#초
#분 == 초
tot =0
for h1 in h:
    if h1 == k: tot+= 3600
    else :
        for m1 in m:
            if k in m1:
                tot+=60
            else:     
                for s1 in s:
                    if k in s1:
                        tot+=1


print(tot)

