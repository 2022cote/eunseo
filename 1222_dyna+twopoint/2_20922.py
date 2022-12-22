
'''
https://www.acmicpc.net/problem/20922 겹치는 건 싫어
'''
N, K = map(int, input().split())
num = list(map(int, input().split()))

sequence = [0] * (max(num) + 1)
left = 0
right = 0
result = 0

while right < N:
    if sequence[num[right]] != K:
        sequence[num[right]] += 1
        right += 1
    else:
        sequence[num[left]] -= 1
        left += 1
    
    result = max(result, right-left)
print(result)