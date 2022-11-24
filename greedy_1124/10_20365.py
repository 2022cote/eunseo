# https://www.acmicpc.net/problem/20365

n = int(input())

RB = str(input())
R_count = RB.count('R')
B_count = RB.count('B')

#BRRBRBRBRRBB
colors = { 'B' : 0, 'R' : 0 } 
colors[RB[0]] +=1 #모두 B로 색칠 
for i in range(1, n): 
    if RB[i] != RB[i-1]:#색 다르면 해당 색의 칠하는 횟수 +1
        colors[RB[i]]+=1

result = min(colors['B'], colors['R'])+1 #칠할 횟수가 더 많은 것을 먼저 전체 칠하고(1) 칠할 횟수가 더 적은 것의 횟수 값(min)을 더한다.
print(result)
