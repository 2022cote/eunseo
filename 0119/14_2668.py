
''' https://www.acmicpc.net/problem/2668	숫자고르기		

'''
def dfs(v,i):
    visited[v]=True
    w=n_dic[v]
    if not visited[w]:
        dfs(w,i)
    elif visited[w] and w==i:
        res.append(w)


n= int(input())
n_dic={}
res=[]
for i in range(1,n+1):
    n_dic[i] = int(input())


 
for i in range(1,n+1):
    visited=[False]*(n+1)
    dfs(i,i)
print(len(res))
print( *sorted(res),sep='\n')