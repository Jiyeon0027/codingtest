#나이트의 이동

import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())
direction=[(1,2),(2,1),(2,-1),(1,-2),(-2,-1),(-1,-2),(-2,1),(-1,2)]
for i in range(tc):
    cnt = 0 
    
    l = int(input())
    visited = [[99999 for _ in range(l)] for _ in range(l)]
    
    st= list(map(int,input().strip().split()))
    end= list(map(int,input().strip().split()))
    
    q= deque()
    q.append(st)
    visited[st[0]][st[1]] = 0
    flag =0
    while q:
        # print(list(q))
        x,y = q.popleft()
        for di in direction:
            dx = x+ di[0]
            dy = y+ di[1]
            if dx<0 or dx>=l or dy<0 or dy>=l:
                continue
            
            if visited[dx][dy] > visited[x][y] +1:
                q.append([dx,dy])
                visited[dx][dy] = visited[x][y]+1
                if dx == end[0] and dy == end[1]:
                    flag= 1
                    break
        print(*visited, sep= '\n')
        if flag == 1 : 
            break
    print(visited[end[0]][end[1]])
    
    
    
