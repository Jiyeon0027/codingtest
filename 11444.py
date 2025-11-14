# 피보나치수 6
# 병합정렬

import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input().strip())

dp = defaultdict(int)
MOD = 1000000007
dp[0] = 0
dp[1] = 1
i=2

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    if not dp[n]:
        if n%2==0:#짝수인 경우
            a = fibo(n // 2 - 1)
            b = fibo(n // 2)
            dp[n] = (2 * a + b) * b % MOD
        else:#홀수 인경우
            a = fibo((n + 1) // 2)
            b = fibo((n - 1) // 2)
            dp[n] = (a * a + b * b) % MOD
    return dp[n]
# while True:
#     dp[i] = dp[i//2]*(dp[i])
fibo(n)
print(dp[n])