#초콜릿 괴도 코코

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph =[]
for _ in range(n):
    graph.append(list(input().strip()))
print(graph)

direction = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs(start):
    q= deque()
    q.append(start)