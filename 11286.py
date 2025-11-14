#절댓값 힙

import sys
from heapq import heappop, heappush
import math
input = sys.stdin.readline

n = int(input())
hq =[]

for _ in range(n):
    x=int(input())
    if x != 0 :
        heappush(hq,( abs(x),x))
    else:
        if len(hq):
            print(heappop(hq)[1])
        else:
            print(0)
    # print(hq)