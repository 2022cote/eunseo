''' https://www.acmicpc.net/problem/20436	ZOAC 3		      '''
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
board = dict()
for i in range(3):
    board.update({keyboard[i][j]: (i, j) for j in range(len(keyboard[i]))})

def dist(finger, target):
    cx, cy = board[finger]
    tx, ty = board[target]
    return abs(cx - tx) + abs(cy - ty)

left, right = input().split()
word = input()
answer = 0
for c in word:
    # 자음 입력
    if (board[c][0] < 2 and board[c][1] < 5) or (board[c][0]==2 and board[c][1] < 4):
        answer += dist(left, c)
        left = c
    # 모음 입력
    else:
        answer += dist(right, c)
        right = c
    answer += 1
print(answer)