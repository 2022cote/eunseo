''' https://www.acmicpc.net/problem/20291	파일 정리		
'''
 
n = int(input())
file = { }
for _ in range(n):
    name = (input().split('.'))[1]
    if name in file : file[name] +=1
    else : file[name] =1 
 #사전순으로 출력
file = sorted(file.items()) 

for i in file :print(i[0],i[1])   