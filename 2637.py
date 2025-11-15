# 장난감 조립

import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
input =sys.stdin.readline

n = int(input())
# 1-n-1 : 기본, 중간
# n : 완제품
m = int(input())

arr = [[[0,0] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    x,y,k = map(int,input().split())
    arr[x][y] = [k,0]

basic = 0
for i in range(m):
    if sum([sum(k) for k in arr[i]]) == 0:
        basic = i

print(*arr, sep = '\n')
print("-----------------")

# for i in range(n, basic,-1):
#     for j in range(n, basic, -1):
#         if arr[i][j][0] > 0 :
            
