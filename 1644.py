#소수의 연속합

import sys
import math
input = sys.stdin.readline

N = int(input())

def find_prime(n):
    prime = [True for _ in range(n+1)]
    prime[0] = False
    prime[1] = False
    
    for p in range(2, round(math.sqrt(n))+1):
        if prime[p] == True:#소수일 경우
            num = 2
            while num*p < n+1:
                prime[p*num] = False
                num +=1
                
    li =[]
    for i in range(n+1):
        if prime[i] == True : 
            li.append(i)
                
    return [i for i in range(n+1) if prime[i] == True]
        
pp = find_prime(N)
cnt =0 

for i in range(len(pp)):
    if pp[i] == N:
        cnt +=1
    for j in range(i+1,len(pp)):
        pp[i] = pp[i]+pp[j]
        if pp[i] == N:
            cnt +=1
            break
        elif pp[i] > N:
            break
print(cnt)