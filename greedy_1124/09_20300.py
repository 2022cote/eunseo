# https://www.acmicpc.net/problem/20300
#근손실의 최솟 값 

n = int(input())#운동기구의 개수
loss = list(map(int, input().split()))#근손실 정도

#PT를 한 번 받을 때의 근손실 정도가 M


up =sorted(loss)
down =sorted(loss ,reverse=True)
tot_loss=0
one_loss=0

if n %2 !=0: #홀수일 시
    del down[0]
    down.append(0)
for i,j in zip(down,up):
    one_loss =  i+j
    if tot_loss < one_loss: tot_loss = one_loss
print(tot_loss)
'''
import sys
n = int(input())
loss = list(map(int, input().split()))
loss.sort()

if n % 2 == 0:#짝수
    m = 0
    for i in range(n//2):
        m = max(t[i]+t[n-i-1], m)
        
else:
    m = t[n-1]
    for i in range(n//2):
        m = max(t[i] +t[n-i-2], m)
        
print(m)

'''
