#미로탐색

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().strip().split())
graph =[]
visited = [[99999 for _ in range(m)] for _ in range(n)]
direction = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    graph.append(list(input().strip()))
# print(graph)

q= deque()
q.append([0,0])
visited[0][0] = 1
while q:
    x,y = q.popleft()
    for di in direction:
        dx = x+di[0]
        dy = y+di[1]
        if dx <0 or dx>=n or dy<0 or dy>=m:
            continue
        if visited[dx][dy] > visited[x][y]+1 and graph[dx][dy] == '1':
            q.append([dx,dy])
            visited[dx][dy] = visited[x][y] + 1
        # print(*visited, sep = '\n')
print(visited[n-1][m-1])