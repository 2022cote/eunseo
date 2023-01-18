''' https://www.acmicpc.net/problem/1969	DNA		

출력
첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 를 출력
둘째 줄에 Hamming Distance의 합
'''
N, M = map(int, input().split())
arr = []
word = ''
dist = 0

for i in range(N):
    arr.append(input())

for i in range(M):
    dic = {}
    for j in range(N):
        if arr[j][i] not in dic:
            dic[arr[j][i]] = 1

        else:
            dic[arr[j][i]] += 1

    ans = list(dic.items())
    ans.sort(key = lambda x : (-x[1], x[0]))
    word += ans[0][0]
    dist += N - ans[0][1]

print(word)
print(dist)