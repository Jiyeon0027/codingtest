# dynamic programming

import sys
input = sys.stdin.readline

storage = list(map(int,input().split()))
n = len(storage)
dp = [0 for _ in range(n)]

dp[0] = storage[0]
dp[1] = storage[1]
dp[2] = max(dp[1] , dp[0]+ storage[2])
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + storage[i])
    
print(dp[n-1])