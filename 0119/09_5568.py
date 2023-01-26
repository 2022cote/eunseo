
''' https://www.acmicpc.net/problem/5568	카드 놓기	
'''	

from itertools import permutations
n = int(input())
arr = []
ans = set()
k = int(input())
for i in range(n):
    arr.append(input())
per = list(permutations(arr, k))
for i in range(len(per)):
    st = ''
    for j in range(len(per[i])):
        st += per[i][j]
    ans.add(st)
ans = list(ans)
print(len(ans))