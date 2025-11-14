#포도주 시식
import sys
input = sys.stdin.readline

dp = [ 0 for _ in range(10001)]

n = int(input())
wine =[0 for _ in range(10001)]
for i in range(n):
   x = int(input())
   wine[i+1] =x
    
dp[0] = 0
dp[1] = wine[1]
dp[2] = wine[1]+wine[2]
dp[3] = max(dp[2],dp[1]+wine[3], dp[0]+wine[2]+wine[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i] ,dp[i-3]+wine[i-1]+wine[i])
# print(dp[:n+1])
# print(max(dp[n]))