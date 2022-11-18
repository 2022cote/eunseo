import sys
from itertools import permutations
input = sys.stdin.readline

k, m = map(int, input().split())
is_prime = [True] * (10**k)

iter_range = int((10**k)**0.5)
for i in range(2, iter_range + 1):
    if is_prime[i]:
        for j in range(i+i, 10**k, i):
            is_prime[j] = False


count = 0
for perm in permutations(range(10), k):
    if perm[0] == 0:
        continue
    num = int(''.join(list(map(str, perm))))
    temp = num
    while temp % m == 0:
        temp = temp//m
    for i in range(2, int(temp**0.5)+1):
        if temp%i == 0:
            if is_prime[i] and is_prime[temp//i]:
                for j in range(2, num//2):
                    if is_prime[j] and is_prime[num-j]:
                        count += 1
                        break
                break
            break
    

print(count)
