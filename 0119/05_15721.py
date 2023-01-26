''' https://www.acmicpc.net/problem/15721	번데기		

입력
게임하는 사람 A명
구하려는 번호 T
구호 "뻔" =0 "데기"=1

1회  ‘뻔 – 데기 – 뻔 – 데기 – 뻔 – 뻔 – 데기 – 데기’ 
2회                        – 뻔 – 뻔 – 뻔 – 데기 – 데기 – 데기
n-1회‘뻔 – 데기 – 뻔 – 데기 – 뻔(x n번) – 데기(x n번)

0101 0011
0101 000111
'''
def sol() :
    n,cnt ,res =1,0,0
    while True:
        n+=1
        li = [0,1,0,1]+[0] * n + [1] * n
        for i in li:
            if a == onezero:
                cnt+=1
            if cnt == t:
                return res
            res +=1
    
    
a = int(input())
t = int(input())
onezero = int(input())

print(sol()%a)