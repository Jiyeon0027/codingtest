# dynamic programming

import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int,input().split())
dp = [INF for _ in range(m+1)]
money =[]
for _ in range(n):
    x= int(input())
    money.append(x)

dp[0] = 0
for i in money:
    for j in range(i, m+1):
        if dp[j-i] != INF:
            dp[j] = min(dp[j], dp[j-i]+1)
print(dp[m])
            
# print(money)
