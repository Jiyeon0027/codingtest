# 구슬탈출
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph =[]
visited = [[0] *m for _ in range(n)]
for _ in range(n):
    graph.append(list(input().strip()))

directions = [(0,1),(0,-1),(1,0),(-1,0)]
red = [0,0]
blue = [0,0]
hole = [0,0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            red = [i,j]
        elif graph[i][j] == 'B':
            blue=[i,j]
        elif graph[i][j] == 'O':
            hole =[i,j]

def go_to_end(x,y,d, graph):
    while True:
        if graph[x][y] == '#' or graph[x][y] =='O':
            return x,y
        graph[x][y] = '#'
        x+=d[0]
        y+=d[1]
    
cnt = 0
q= deque()
q.append([red[0], red[1], blue[0],blue[1]])
FLAG =1

while q:
    rx,ry,bx,by,d = q.popleft()
    for i, j in directions:
        nx,ny = go_to_end(rx,ry,[i,j],graph)
        nbx,nby = go_to_end(bx,by,[i,j],graph)
        
        if nx == nbx and ny == nby:#같은곳으로 이동한 경우
            if graph[nx][ny] == 'O':
                FLAG = 0
            else:
                graph[nx][ny] = 'R'
                graph[nx-i][ny-i] = 'B'
        else:#다른곳으로 이동한 경우
            if graph[nx][ny] == 'O':
                FLAG = 1
            else:
                graph[nx][ny] = 'R'
                graph[nx][ny] = 'B'
        
        print(f'nx:{nx}, ny:{ny}, nbx: {nbx}, nby:{nby}')
        print(*graph, sep='\n')
        q.append([nx,ny])
        blue = [nx-i, ny-j]
        print(f"blue : {blue}")
