'''https://www.acmicpc.net/problem/2579

계단 오르기
 
문제

계단 오르는 데는 다음과 같은 규칙이 있다.

한 번에 1 or 2개 가능
연속 3개 X      단, 시작점: 포함X
마지막 도착 계단은 반드시 밟아야 한다.
총 점수의 최댓값을 구하는 프로그램을 작성하시오.

입력
입력의 첫째 줄에 계단의 개수가 주어진다.
둘째 줄부터 계단 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 
계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

출력
첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

예제 입력           출력 75
6

10 *
20 *
15
25 *
10
20 *

'''

def cal(n):
    score =[int(input()) for _ in range(n)]
    if n <3 : return sum(score)
    dp= [0]*(n +1)
    dp[1]=score[0]
    dp[2]=score[1]+score[0]
    for i in range(3,n+1):
        dp[i] = max(dp[i-2],dp[i-3]+score[i-2])+score[i-1];
    return dp[n]

n = int(input())

print(cal(n) )


