#https://www.acmicpc.net/problem/1343
#문제
'''
민식이는 다음과 같은 폴리오미노 2개를 무한개  AAAA와 BB를 가진다
'.'와 'X'로 이루어진 보드판 : 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮고,  '.'는 폴리오미노 덮지 X

입력 : 첫째 줄에 크기가 최대 50인 보드판이 주어진다.
출력 : 첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.

예제 입력           예제 출력
XXXXXX              AAAABB
XX.XX               BB.BB
XXXX....XXX.....XX  -1
X                   -1
'''
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board: print(-1)
    
else:
    print(board)


    '''
s = str(input())
if '.' in s:    
    li = s.split('.')
else : li = [s]

output= ""
for i in range(len(li)): 
    #'' 없는데 i 변화하면 넣어줘야함 
    if i >0 :output= output +"."
    if li[i] =='' : output= output +"."
    elif len(li[i]) %2 ==1: 
        output = -1
        break
    else : 
        four = len(li[i]) //4  
        div =len(li[i]) % 4
        if div ==0:
            output = output+ "AAAA" * four
        else : 
            output =output+"AAAA"*four +"BB"*int(div/2)
    
print(output)'''