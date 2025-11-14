# 카드게임
# dp

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int,input().strip().split()))

    turn = True if n%2==1 else False 
    #홀수일 경우 근우로 끝나므로 근우에게 점수주고 시작
    
    dp = [[0 for _ in range(n)] for _ in range(n)]
            
    for size in range(n):
        for i in range(n-size):
            if size == 0:
                if turn:
                    dp[i][i] = cards[i]
            elif turn : #근우 차례 일때
                dp[i][i+size] = max(dp[i][i+size-1]+cards[i+size], dp[i+1][i+size]+cards[i])
            else: #명우 차례일때
                dp[i][i+size] = min(dp[i][i+size-1], dp[i+1][i+size])
        turn = not turn
    
    print(dp[0][n-1])
    