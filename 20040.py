# 사이클 게임

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
parents = [i for i in range(n)]
# visited = [False for _ in range(n)]

def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union(a,b):
    root_a = find_parents(a)
    root_b = find_parents(b)
    
    if root_a < root_b: 
        parents[root_b] = root_a
    else:
        parents[root_a] = root_b

result = 0
# graph = [[] for _ in range(n)]
for idx in range(1,m+1):
    a,b = map(int,input().split())
    
    # union(a,b)
    # if parents[a] == parents[b]:
    #     result = idx
    #     break
    
    if find_parents(a) != find_parents(b):
        union(a,b)
    else:
        result = idx
        break

print(result)
    