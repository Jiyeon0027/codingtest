#N번째 큰수

import sys
input = sys.stdin.readline

from heapq import heappop, heappush

n = int(input())
chart = []
for _ in range(n):
    li = list(map(int,input().strip().split()))
    for l in li:
        if len(chart)< n:
            heappush(chart, l)
        elif chart[0]< l :
            heappush(chart, l)
            heappop(chart)
    print(chart)

print(chart[0])
            