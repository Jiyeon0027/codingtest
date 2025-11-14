#특정한 최단경로

import sys
from heapq import heappop, heappush
input= sys.stdin.readline


n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
v1,v2 = map(int,input().split())
# 1-v1-v2-n
# 1-v2-v1-n

INF = sys.maxsize

def dijkstra(start, end):
    min_dist = [INF for _ in range(n+1)]
    hq=[]
    heappush(hq, (0, start))
    min_dist[start] = 0
    while hq:
        now_w, now_node = heappop(hq)
        if min_dist[now_node] < now_w:
            continue
        for nxt_node, next_w in graph[now_node]:
            if min_dist[nxt_node] > min_dist[now_node] + next_w:
                min_dist[nxt_node] = min_dist[now_node] + next_w
                heappush(hq, (min_dist[nxt_node], nxt_node))
                # print(min_dist)
    return min_dist[end]

second = dijkstra(v1,v2)
stTov1 = dijkstra(1,v1)
v2Toend = dijkstra(v2,n)
stTov2 = dijkstra(1,v2)
v1Toend = dijkstra(v1,n)

first = stTov1
end = v2Toend

if stTov1+v2Toend > stTov2+v1Toend:
    first = stTov2
    end = v1Toend

if first == INF or second == INF or end== INF:
    print(-1)
else:
    print(first+second+end)