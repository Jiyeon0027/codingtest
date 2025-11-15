# 다익스트라 - 최단경로 알고리즘

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF for _ in range(n+1)]

for _ in range(m):
    x,y,d = map(int,input().split())
    graph[x].append((y,d))
    graph[y].append((x,d))

def dijkstra(start):
    hq = []
    heappush(hq, (0, start))
    distance[start] = 0
    
    while hq:
        dist , cur = heappop(hq)
        print(f"cur : {cur}, dist : {dist}")
        if distance[cur] < dist: # 이미 방문해서 최단거리가 더 짧게 갱신 되어있으면 지나가기
            continue
        for nxt, nxt_d in graph[cur]:
            if distance[nxt] > dist + nxt_d :
                distance[nxt] = dist + nxt_d
                print(distance)
                heappush(hq, (distance[nxt], nxt))
                
dijkstra(start)