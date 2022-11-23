#https://www.acmicpc.net/problem/1758
#돈 - (받은 등수 - 1) 만큼의 팁
#민호, 재필, 주현 순서로 줄
#민호 3-(1-1) = 3원, 재필  2-(2-1) = 1원, 주현 1-(3-1) = -1원(음수는 0으로)
#팁을 3+1+0=4원
import sys
input = sys.stdin.readline
#입력
n = int(input())

li = [ int(input()) for _ in range(n)] 
li.sort(reverse=True)

sum =0
for rank in range(n):
    a = li[rank]-rank#돈 - (받은 등수 - 1) 만큼의 팁
    if a >0 : sum+=a
print(sum)