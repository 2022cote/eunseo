''' https://www.acmicpc.net/problem/18511	큰 수 구성하기		
'''
def backTracking(num):
    global ans
    if num > N:
        return
    ans = max(ans,num)
    for i in K:
        num = num * 10 + i
        backTracking(num)
        num = (num - i) // 10

N, C = map(int, input().split())
K = list(map(int, input().split()))
ans = 0
backTracking(0)
print(ans)