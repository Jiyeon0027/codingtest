# 바이러스

import sys
from collections import deque
input = sys.stdin.readline

comp = int(input())
n = int(input())
visited = [0 for _ in range(comp+1)]
map_comp =[[] for _ in range(comp+1)]

for _ in range(n):
    x,y = map(int,input().split())
    map_comp[x].append(y)
    map_comp[y].append(x)
    
# print(map_comp)
q= deque()
q.append(1)
visited[1] = 1
while q:
    c = q.popleft()
    for i in map_comp[c]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1
    # print(q)
    # print(visited)

print(sum(visited)-1)