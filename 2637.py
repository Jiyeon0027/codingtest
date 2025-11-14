# 장난감 조립

import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
input =sys.stdin.readline

n = int(input())
# 1-n-1 : 기본, 중간
# n : 완제품
m = int(input())

arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x,y,k = map(int,input().split())
    arr[x][y] = k

count = [0] * (n+1)

def check_sub(part, mult):
    if sum(arr[part]) == 0 : # 기본부품
        count[part] += mult 
        return
    
    for sub in range(1,n+1):
        if arr[part][sub] > 0:
            check_sub(sub,mult * arr[part][sub])
    
    
check_sub(n,1)
for i in range(1,n):
    if sum(arr[i]) ==0:
        print(f"{i} {count[i]}")