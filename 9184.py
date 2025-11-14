#신나는 함수 실행

import sys
input = sys.stdin.readline
dp =[[[0 for _ in range(5)] for _ in range(21)] for _ in range(21)]
# print(dp)

for x in range(21):
    for y in range(21):
        for z in range(21):
            if x==0 or y==0 or z==0:
                dp[x][y][z] =1
            elif x<y and y<z:
                dp[x][y][z] = dp[x][y][z-1] + dp[x][y-1][z-1] - dp[x][y-1][z]
            else:
                dp[x][y][z] = dp[x-1][y][z] + dp[x-1][y-1][z] + dp[x-1][y][z-1] - dp[x-1][y-1][z-1]

# print(*dp,sep = '\n')
while True:
    a,b,c = map(int,input().strip().split())
    if a==-1 and b== -1 and c==-1:
        break
    
    if a<=0 or b<=0 or c<=0:
        print(f'w({a}, {b}, {c}) = 1')
    elif a>20 or b>20 or c>20:
        print(f'w({a}, {b}, {c}) = {dp[20][20][20]}')
    else:
        print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')