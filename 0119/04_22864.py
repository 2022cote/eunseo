''' https://www.acmicpc.net/problem/22864	피로도		
한 시간 일 : 피로도 A     일 B 만큼 처리
한 시간 휴식 : 피로도 -C  
피로도 <M

24h'''
a,b,c,m = map(int, input().split())
if a >m : 
    print(0)
    exit(0)
stress=0
work =0
for i in range(24):
    if stress+a < m:
        stress +=a
        work +=b
    else : stress -=c
print(work)