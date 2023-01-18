''' https://www.acmicpc.net/problem/2231	분해합		

245의 분해합은 256(=245+2+4+5)이 된다. 
 출력 : 198 198+1+9+8 =입력 :216
'''
n = int(input())

for i in range(n//10,n+1):
    num = sum(map(int, str(i)))
    num_s = i +num

    if n == num_s : 
        print(i)
        break
    if i == n : 
        print(0)
        break


