''' https://www.acmicpc.net/problem/20546	🐜 기적의 매매법 🐜		'''
m = int(input()) 

BNP_m,BNP_j,BNP_s = m,0,0 
TIM_m,TIM_j,TIM_s = m,0,0  
 
MD = list(map(int,input().split()))
a=0
for i in MD:

    # BNP  
    BNP_j += BNP_m//i  
    BNP_m = BNP_m%i  

    # TIMING 
    if a >= 3: 
        # 3일 연속 하락
        if MD[a-3] > MD[a-2] > MD[a-1]: 
            TIM_j += TIM_m// i  
            TIM_m = TIM_m% i 
        # 3일 연속 상승             
        elif MD[a-3] < MD[a-2] < MD[a-1]:  
            TIM_m += TIM_j*i 
            TIM_j = 0
    a+=1           

        
BNP_s = BNP_m +BNP_j*MD[-1]
TIM_s= TIM_m+TIM_j*MD[-1]

if BNP_s > TIM_s:     print('BNP')
elif BNP_s < TIM_s:     print('TIMING')
else:    print('SAMESAME')