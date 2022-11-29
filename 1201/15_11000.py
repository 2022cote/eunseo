'''
https://www.acmicpc.net/problem/11000
문제
김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데,
 최소의 강의실을 사용해서 "모든 수업을 가능"하게 해야 한다. 
참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)
수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.

입력                출력
3 N개의 수업
s e

'''
import sys
import copy
input = sys.stdin.readline
N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

time.sort(key = lambda x: (x[1], x[0]))
t2 = copy.deepcopy(time)
cnt = 1

while len(time) >1 :
    end = time[0][1]#가장 처음 끝나는 시간 
    del t2[0]
    for i in time:
        if i[0] >= end:#start가 end보다 클 때 회의실 사용 가능
            end = i[1]
            t2.remove(i)
            if len(t2) == 1: break
    N = len(t2)
    time =t2
            
    cnt +=1

#출력 : 강의실 개수
print(cnt)