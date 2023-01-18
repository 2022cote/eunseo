''' https://www.acmicpc.net/problem/2798	블랙잭	
블랙잭 : 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임
N장의 카드를 모두 숫자가 보이도록 바닥에 놓은 후에 딜러는 숫자 M을 크게 외친다.

플레이어 :N장의 카드 중에서 합이 M을 넘지 않으면서 M과 가까운 3장의 카드를 골라라

입력
첫째 줄 : 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)
둘째 줄 : 카드 


'''

def sol(m):
    tsum =0 #3장의 최솟값
    for x in range(n-2):
        for y in range(x+1,n-1):
            for z in range(y+1,n):
                s2 =card[z]+card[x] +card[y]
                if s2 <= m  and tsum <s2: tsum = s2
    return tsum

n,m = map(int, input().split())

card = sorted(list(map(int, input().split())))

print(sol(m))

