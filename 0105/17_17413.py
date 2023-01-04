
''' https://www.acmicpc.net/problem/17413	단어 뒤집기 2		
'''
S = list(input()) 
tot = len(S)
li_s =[]
i=0
while i < tot:
    if  S[i] == '<':
        for j in range(i,tot):
            if S[j] =='>':  
                li_s.append(S[i:j+1])
                break
        i = j+1
    for a in range(i,tot):
        if S[a] =='<' or S[a] ==' ': 
            qa=S[i:a]
            li_s.append(S[a-1:i-1:-1])
            break 
    i =a+1    
    if S[tot-1] != '>':li_s.append(S[a-1:i-1:-1])

    
    

print(*li_s,sep='')
    


