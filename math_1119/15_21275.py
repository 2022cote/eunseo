def trans(st , notation):
    temp = 0
    for i in range(len(st)):
        temp += ((int(notation)**i) * numbers[st[-1-i]])
    return temp

#공백으로 a b
a,b=map(str,input().split())

#숫자
numbers = {str(i):i for i in range(10)}
# 알페벳 a부터
for i in range(26):
    numbers[chr(97+i)] = i+10

cnt = 0
ans = [0, 0]
for i in range(numbers[max(list(a))]+1, 37):
    for j in range(numbers[max(list(b))]+1, 37):
        if i == j:
            continue
        if trans(a, i) == trans(b, j):
            if trans(a, i) >= 2**63:
                continue
            ans[0] = i
            ans[1] = j
            cnt += 1

if cnt == 0:
    print("Impossible")
elif cnt > 1:
    print("Multiple")
elif cnt == 1:
    print(trans(a, ans[0]), ans[0], ans[1])