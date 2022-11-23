#https://www.acmicpc.net/problem/11399
#ATM앞에 N명의 사람들이 돈을 인출하는데 걸리는 시간의 최솟값 구하기
#if , P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2 
# 1 2 3 4 5로 정렬

import sys
input = sys.stdin.readline

n = int(input())

 #몇 분이 걸리는지 
num_list = list(map(int, input().split()))
num_list.sort()#작은수 부터 정렬 

time=0
time_list = []

for t in num_list:
    time += t# 다음사람이 얼마나 걸리는지 = 전의 시간+ 현재 Pn의 걸리는 시간
    time_list.append(time)

result = sum(time_list)
print(result)