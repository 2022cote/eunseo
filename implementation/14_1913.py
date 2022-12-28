''' https://www.acmicpc.net/problem/1913	    달팽이	          '''

n = int(input())
num = int(input())
dx = [0,1,0,-1,0]
dy = [1,0,-1,0,0]

a = [[0]*n for _ in range(n)]

x,y = n//2, n//2
a[x][y] = 1

size = n//2
s = 2
tmp = 2
for _ in range(size):
	x -= 1
	
	for k in range(4):
		for _ in range(s):
			a[x][y] = tmp
			x,y = x+dx[k],y+dy[k]
			tmp+=1
		x,y = x-dx[k],y-dy[k]
		x,y = x+dx[k+1],y+dy[k+1]
	s+=2
for line in a:
	print(" ".join(map(str,line)))

for i in range(n):
	for j in range(n):
		if a[i][j] == num:
			print(i+1,j+1)