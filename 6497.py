#전력난

import sys
from heapq import heappush, heappop
input= sys.stdin.readline

while True:
    m,n = map(int,input().split())
    if m==0 and n==0:
        break
    
    roads= [[] for _ in range(m)]
    visited = [0 for _ in range(m)]
    all_dist = 0 
    
    for i in range(n):
        x,y,z = map(int,input().split())
        roads[x].append((y,z))
        roads[y].append((x,z))
        all_dist += z

    for i in range(m):
        roads[i].sort()
    # print(roads)
    
    hq =[]
    heappush(hq, [0,0]) #시작한 집번호 0 , 거리 0
    min_dist = 0

    while hq :
        dist, cur_x = heappop(hq)
        # print(hq)
        # print(visited)
        if visited[cur_x] == 1: 
            continue
        visited[cur_x] = 1
        min_dist += dist
        
        for next_x, next_d in roads[cur_x]:
            if visited[next_x]== 0:
                heappush(hq, [next_d, next_x])
        
    print(all_dist - min_dist)