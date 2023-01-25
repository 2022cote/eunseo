
''' https://www.acmicpc.net/problem/12919	A와 B 2
 
 '''		
S=list(input())
T=list(input())
def dfs(t): 
    if t==S:
        print(1)
        exit(0)
    if len(t)==0: return 0
    if t[-1]=='A':dfs(t[:-1])
    if t[0]=='B': dfs(t[1:][::-1])
dfs(T)