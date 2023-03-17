
''' https://www.acmicpc.net/problem/14501	퇴사		

            '''
n = int(input())
li = [list(map(int, input().split())) for i in range(n)]
 
answer = [0] * (n + 1)

 

for i in range(n - 1, -1, -1):
    if li[i][0] + i > n:  answer[i] = answer[i + 1]
    else: answer[i] = max(li[i][1] + answer[i + li[i][0]], answer[i + 1])
        
print(answer[0])