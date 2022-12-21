'''
https://www.acmicpc.net/problem/16953

문제
정수 A를 B로 바꾸려고 한다. 
가능한 연산 : 2를 곱한다. OR 1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력
첫째 줄에 A, B (1 ≤ A < B ≤ 10^9)가 주어진다.

출력
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

입력        출력 
2 162        5      2 → 4 → 8 → 81 → 162
4 42        -1
100 40021    5      100 → 200 → 2001 → 4002 → 40021
'''
import sys
input = sys.stdin.readline

def sol(A,B):
    cnt =0 
    while True:      
        if  A >B : return -1  #A가 B보다 크면 이미 X
        elif B % 2== 0:   B = B//2 #첫 번째 조건 *2
        elif int(str(B)[-1]) == 1: B = B//10 #두번째 조건 뒤에 1넣기
        else :return -1 

        cnt+=1
        if B == A :break
    return cnt+1
    

A,B = map(int , input().split())
print(sol(A,B))

