#빙산

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph=[]
direction = [(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
def bfs(graph, x,y):
    q = deque()
    q.append([x,y])
    while q:
        cx,cy = q.pop()
        for dx,dy in direction:
            ax = dx +cx
            ay = dy +cy
            if graph[ax][ay] !=0 and visited[ax][ay] == -1: #non-visited
                visited[ax][ay] = 0
                q.append([ax,ay])

def check_around_zero(x,y):
    count =0
    for dx,dy in direction:
        cx = dx +x
        cy = dy +y
        if graph[cx][cy] == 0:
            count+=1
    return count

year = 0 
flags_for_ice =0
while True:
    year +=1
    seperated =0
    flags_for_ice=0
    graph_copy = [[0]*m for _ in range(n)]
    
    for i in range(1,n-1): #300
        for j in range(1,m-1): #300
            if graph[i][j] >0 :
                count = check_around_zero(i,j) #4
                # print(f'{i},{j} - count : {count}')
                graph_copy[i][j] = graph[i][j]-count
                if graph_copy[i][j] <0 :
                    graph_copy[i][j] = 0
    # print(*graph_copy, sep='\n')
    # print()
    graph = graph_copy
        
    visited = [[-1]*m for _ in range(n)]
    for i in range(1,n-1):
        for j in range(1,m-1):
            if graph[i][j] >0 and visited[i][j] == -1:
                bfs(graph,i,j)
                # print(*visited,sep='\n')
                seperated +=1
                # print(seperated)
            if graph[i][j] >0:
                flags_for_ice =1
            
    if seperated >=2 or flags_for_ice == 0: #빙하가 다 녹거나 분리되면 반복문 종료
        break

if flags_for_ice ==0:
    print(0)
else:
    print(year)