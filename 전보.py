# 최단 거리 문제

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n,m,c = map(int,input().split())
# 한 도시에서 여러 지점으로 보내므로 다익스트라

city_path = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int,input().split())
    city_path[x].append((y,z))
    
INF = sys.maxsize
distance = [ INF for _ in range(n+1)]

def dijkstra(start):
    hq =[]
    heappush(hq,(0, start))
    distance[start] = 0 
    while hq:
        dist, now = heappop(hq)
        if dist > distance[now]:
            continue
        for i in city_path[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(hq, (cost,i[0]))
                
dijkstra(c)
cnt =0 
max_city = -1
for i in range(1, n+1):
    if distance[i]>0 and distance[i] < INF:
        cnt +=1
        max_city = max(distance[i], max_city)
        
print(cnt, max_city)