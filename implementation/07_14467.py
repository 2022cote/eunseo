''' https://www.acmicpc.net/problem/14467	소가 길을 건너간 이유 1

존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 

입력
첫 줄에 관찰 횟수 N이 주어진다. N은 100 이하의 양의 정수이다. 
다음 N줄에는 한 줄에 하나씩 관찰 결과가 주어진다. 
관찰 결과는 소의 번호와 위치(0 또는 1)로 이루어져 있다.

출력
첫 줄에 소가 길을 건너간 최소 횟수를 출력한다.

	'''	 
n = int(input())
cow = {}
count = 0
 
for _ in range(n):
    a,b = map(int, input().split())
    if a not in cow:
        cow[a] = b #추가
    else:
        if cow[a] != b:            
            cow[a] = b
            count +=1
print(count)