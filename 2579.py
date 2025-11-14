#계단 오르기

# 1. 한계단 또는 두계단
# 2. 연속된 3계단 오를수 없음
# 3. 마지막 계단은 반드시 올라야 함

# 1-2-4
# 1-3-4

import sys
input= sys.stdin.readline

n = int(input())
stairs =[0 for _ in range(n+1)]
for i in range(1,n+1):
    stairs[i] = int(input())
INF = sys.maxsize

dp = [[0,0] for _ in range(n+1)]
dp[0] = [0,0] # 앞은 그앞의 것을 지나온것, 뒤는 뛰어 넘은것
if n >=1:
    dp[1] = [stairs[1], stairs[1]]
if n>=2:
    dp[2] = [stairs[1]+stairs[2], stairs[2]]
if n>=3:
    dp[3] = [stairs[2]+ stairs[3], max(dp[1])+ stairs[3]]
    
for i in range(3, n+1):
    dp[i][0] = dp[i-1][1] + stairs[i]
    dp[i][1] = max(dp[i-2]) + stairs[i] 

print(max(dp[n])) 


