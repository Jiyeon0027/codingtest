#파일 합치기

#뭔가 최단거리찾기 느낌
import sys
from heapq import heappop, heappush, heapify
from collections import deque

input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    k = int(input())
    k_li = list(map(int,input().split()))
    
    dp = [[0]*k for _ in range(k)]
    
    for i in range(k):
        dp[i][i] = k_li[i]
    
    for i in range(k):
        for j in range(1,k):
            