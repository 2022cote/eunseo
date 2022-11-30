#https://www.acmicpc.net/problem/11508
#2+1 행사로  가격 높은 2개 가격만 받음
#sort 사용해서 값이 작은거 del 해주고 나머지 더하기
#입력 :655 554
#출력 :11   10 = 21
import sys
input = sys.stdin.readline

#입력
n = int(input())

li = [int(input()) for _ in range(n)]
li.sort(reverse=True)#가격 낮춰야하므로 높은 금액부터 
tot =0
for i in range(n//3):#2+1이므로 입력된 수 /3 만큼만 돌리기
    tot += li[i*3] +li[i*3+1]#가격 높은 2개 
if n % 3 >0:#만약 정수값이 아니고
    tot +=li[-1] #나머지 1개일 때
    if n%3 ==2 : tot+=li[-2]#나머지 2개 일때
    
print(tot)
