''' https://www.acmicpc.net/problem/10994	별 찍기 - 19		  

n = int(input()) -1

for i in range(n):
    print("* " *i +"*"*(1+4*(n-i)) +"*"*i)
    print("* " *(1+i) +"*"*(1+4*(n-i-1)) +"*"*(1+i))

print("* " *(2*n+1))

'''
def add_star(ptn):
    return "* " + ptn + " *"

def star(n):
    if n == 1:
        return ["*"]
    else:
        return ["*"*(4*n-3), "*"+" "*(4*n-5)+"*"]  + list(map(add_star, star(n-1))) + ["*"+" "*(4*n-5)+"*", "*"*(4*n-3)]

print("\n".join(star(int(input()))))