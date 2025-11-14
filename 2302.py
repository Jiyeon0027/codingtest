# 극장 좌석
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
seats = []

prev = 0

for _ in range(m):
    vip = int(input())
    seats.append(vip-prev-1)
    prev = vip

seats.append(n-prev)

dp = [ [0,0] for _ in range(41)]
dp[1] = [1,0]
dp[2] = [1,1]

for i in range(3, 41):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
    
answer = 1
# print(seats)
for non_vip in seats:
    if non_vip == 0:
        continue
    answer *=sum(dp[non_vip])
print(answer)