#아기상어

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
#가장 처음 아기상어의 크기 =2
size =2
#자기 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음
#자신의 크기보다 작은 물고기 먹기 가능
#크기가 같은 수의 물고기를 먹을때 크기가 1 증가

graph=[]
st_x=0
st_y=0
fish_map =[]
dist = [[-1 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().split())))

print(graph)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            st_x,st_y=i,j
        elif graph[i][j]>0:
            fish_map.append([graph[i][j], i ,j, False]) #믈고기 크기와 같이 저장
print(fish_map)
direction = [(0,-1),(-1,0),(1,0),(0,1)]

def dfs(x,y, dist):
    print(x,y,dist)
    if graph[x][y] >0 and graph[x][y]<size:
        #물고기 삭제 후 종료
        return dist
    for dx,dy in direction:
        cx = dx+x
        cy = dy+y
        if cx<0 or cx>=n or cy<0 or cy>=n:
            continue
        if graph[cx][cy] <= size and graph[cx][cy]>=0:
            graph[cx][cy] = -1# check visited
            dfs(cx,cy,dist+1)

def bfs(x,y):
    q= deque()
    q.append([x,y])
    dist[x][y] = 0#  시작 지점
    while q:
        cx,cy = q.pop()
        for dx,dy in direction:
            cx = dx+x
            cy = dy+y
            if cx<0 or cx>=n or cy<0 or cy>=n:
                continue
            if graph[cx][cy] <= size and graph[cx][cy]>=0:
                dist[cx][cy]  = dist[x][y] +1
                
# while fish_map:
#     if size < fish_map[0]:
        