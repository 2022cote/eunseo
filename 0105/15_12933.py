''' https://www.acmicpc.net/problem/12933	오리		


참고 -https://nahwasa.com/entry/%EC%9E%90%EB%B0%94-%EB%B0%B1%EC%A4%80-12933-%EC%98%A4%EB%A6%AC-java
quackquackquack -> 3번 났지만 '최소'이고 한마리가 낼 수 있으므로 1마리
qquackuack -> 오리는 무조건 quack 순서로 내므로 이건 2마리가 필요하다.
qqauckuack -> quack 하나는 가능한데, 나머지 한번은 qauck가 된다. 이건 오리가 울 수 있는 소리가 아니니 녹음이 올바르지 않은 경우이다.
quackqquuaacckk -> 처음 quack 이후 quack가 겹치는데, 그 중 한마리는 처음 quack랑 같은녀석으로 칠 수 있다. 그러니 2마리이다.
'''
def ducks(): 	
    sound = {'q':0,'u':1,'a':2,'c':3,'k':4}
    duck = input()    
    if len(duck)%5: return -1
 
    #totalmax 2500
    tot = [0] *500
    ans = set()
    for i in duck:
        for j in range(500):
            if tot[j] == sound[i]:
                tot[j] +=1
                if tot[j] ==5:
                    tot[j] =0
                    ans.add(j) 
                break
    if len(ans) and sum(tot)==0 : return len(ans)
    else :return -1




print(ducks())