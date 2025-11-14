#연속합
import sys
input = sys.stdin.readline

n = int(input().strip())
list_n = list(map(int,input().strip().split()))
dp= [0 for _ in range(n)]
dp[0] = list_n[0]

for i in range(1,n):
    dp[i] = max(list_n[i],dp[i-1]+list_n[i])

print(max(dp))