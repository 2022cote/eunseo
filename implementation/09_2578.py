''' https://www.acmicpc.net/problem/2578	    빙고
입력
1~5 : 빙고판에 쓰여진 수
6~10  :사회자가 부르는 수

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"
3개의 빙고 완성

'''
bingo = [ list(map(int, input().split())) for _ in range(5)]
out = [ list(map(int, input().split())) for _ in range(5)]
 

check = [0] * 12 #  0~4: row / 5~9: col / 10, 11: 대각
line = 0
flag = False
for n in range(25):  
    if flag == True:  break
    for i in range(5): 
        if flag == True:  break
        for j in range(5):
            if flag == True:     break
            if out[n] == bingo[i][j]:  
                bingo[i][j] = 0  
                check[i] += 1 
                check[j+5] += 1  
                if i == j: #대각
                    check[10] += 1
                if i + j == 4: #대각
                    check[11] += 1
                for c in range(12): 
                    if check[c] == 5: 
                        check[c] = 0 
                        line += 1 
                        if line == 3:
                            flag = True
                            break
print(n)