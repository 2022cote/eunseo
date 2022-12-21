
'''
https://www.acmicpc.net/problem/20922 겹치는 건 싫어
'''
N,K = map(int, input().split())
num = list(map(int, input().split()))
cnt = []        

    #start와 end사이에 겹치는 수가 K개 이하일 때는 end를 늘리며
    # 최대 길이를 늘리고
    # K개 초과일 때는 begin를 늘리며 겹치는 수가 빠질때까지 begin을 증가
ans = 0
end =1
for be in range(N) :
    while(end <=N and cnt[num[end]] < K):
        cnt[num[end]]+=1
        end +=1
    ans = max(end-be,ans)    
    cnt[num[be]] -=1
print(ans)
