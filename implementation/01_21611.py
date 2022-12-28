''' https://www.acmicpc.net/problem/21611	마법사 상어와 블리자드		'''
N,M = map(int,input().split())
field = [list(map(int,input().strip().split())) for _ in range(N)]
skills = [list(map(int,input().strip().split())) for _ in range(M)]#상어 스킬
direction = [[0,0],[0,-1],[0,1],[-1,0],[1,0]]#상하좌우
broken_marble = [0,0,0]#파괴한 구슬
indexing = {}


