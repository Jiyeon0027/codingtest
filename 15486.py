#퇴사2

import sys
input = sys.stdin.readline
n=int(input())

tp = [[]]
dp = [0 for _ in range(n+2)]

for _ in range(n):
    tpi = list(map(int,input().split()))
    tp.append(tpi)
# print(tp)

dp[n+1] = 0
for i in range(n,0,-1):
    if n+1 >= tp[i][0]+i: # 상담 가능
        dp[i] = max(tp[i][1]+dp[i+tp[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[1])

# for i in range(2,n+1):
#     k = i-1
#     while k>0:
#         print(f'i= {i},k = {k}')
#         print(f'tp[k]:{tp[k]}')
#         if tp[k][0] + k <= i:
#             dp[i] = max(tp[i][], tp[i]+dp[k])
#         k-=1
#         print(dp)