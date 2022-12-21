'''
https://www.acmicpc.net/problem/11660 
구간 합 구하기 5

문제
N×N개의 수가 N×N 크기의 표에 채워져 있다. 
(x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램

N = 4
1	2	3	4
2	3	4	5
3	4	5	6
4	5	6	7
(2, 2)부터 (3, 4)까지 합  
 3+4+5 +4+5+6 = 27 
(4, 4)부터 (4, 4)까지 합 :7

표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

입력
첫째 줄: 표의 크기 N | 합을 구해야 하는 횟수 M
다음줄이 표
마지막 M 개의 줄 xy 좌표값

출력
총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.

예제 입력 1 
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
예제 출력 1 
27
6
64
예제 입력 2 
2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
예제 출력 2 
1
2
3
4
'''
n,m = map(int ,input().split())
dp = [[0 for col in range(n+1)] for row in range(n+1)]
arr = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + arr[i][j]


for i in range (m):    
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1] )
    