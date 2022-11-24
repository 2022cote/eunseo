#https://www.acmicpc.net/problem/14916
#거스름돈 2x+5y =input의 최소 개수 if 불가 : -1 출력
#입력 14 | 5원 2개  2원 2개 | 출력: 4
#입력 13 | 5원 1개  2원 3개 | 출력: 5
# 2 4 5 6 7 8 9 10 11 12 13 14로 1, 3제외한 모든 수 가능 

def change(n,n5):  
    if n == 1 or n==3 :return -1 # 만약 1원 or 3원일 때는 불가하므로  -1
    elif n5 % 2 ==0:return n//5+ n5//2 #n5는 나머지 값이므로 2로 나누는게 가능하다면  return 5원 +  2원 개
    else: return (n//5)-1 + (n5+5)//2 

n = int(input())

n5 = n %5 # 5원 나머지
print(change(n,n5))


'''
s = [-1]
div = n //5#5원 나머지
while(div >-1):  
    a =list(str(n))[-1]
    if  a == 1 or a ==3:         
        break
    x = n - div*5
    x2 = x/2
    if x % 2 ==0:
        del s[0]
        s.append(div+x2)

        
        
    div -=1
s.sort()
print(s[0])
    
'''
