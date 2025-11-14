# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

dp = [ INF for _ in range(n+1)]
dp[1] = 0

for i in range(n+1):
    if i%5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1)
    
    dp[i] = min(dp[i], dp[i-1]+1)
    
print(dp[n])   