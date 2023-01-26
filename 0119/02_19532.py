''' https://www.acmicpc.net/problem/19532	수학은 비대면강의입니다		

ax + by = c
dx + ey = f
1 3 -1 4 1 7
x+3y = -1 4x+12y = -4
-4x+y = 7
11y =-11

'''


a,b,c,d,e,f = map(int,input().split())
x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x,y)

''' 0으로 나눌 때 X 인거 있음 
from math import lcm,trunc

ad = lcm(a,d) 
if a ==0:
    y1 = c/b
    x1= (f-e*y1)/d
else :
    y1 = (c* (ad /a)-f*(ad/d)) /(b* (ad /a)-e*(ad/d))
    x1 = (c-b*y1)/a
print(trunc(x1),trunc(y1))
'''