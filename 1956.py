#운동

import sys
import heapq
input= sys.stdin.readline

v,e = map(int,input().strip().split())
graph ={}

for _ in range(e):
    a,b,c = map(int,input().strip().split())
    if a not in graph:
        graph[a] = []
    graph[a].append((b,c))

INF  = int(1e9)

def dijkstra(start):
    dist = [INF for _ in range(v+1)]
    hq=[]
    heapq.heappush(hq, (0,start))
    dist[start] = 0
    while hq:
        cur_cost, cur_node = heapq.heapop(hq)
        if dist[cur_node] < cur_cost:
            continue
        for nxt_node, weight in graph[cur_node]:
            if dist[nxt_node] > dist[cur_node] + weight:
                dist[nxt_node] = dist[cur_node] + weight
                heapq.heappush(hq, (dist[nxt_node], nxt_node))
    # print(dist)
    return dist

min_dist = INF    

# 각 정점에서 다익스트라 수행
for u in range(1, v+1):
    dist = dijkstra(u)
    # u → v → u 로 사이클 확인
    for v_, weight in graph[u]:
        # 간선 (u → v_)를 이용해서 사이클 완성: v_ → ... → u
        if dist[v_] != INF:
            cycle_len = dist[v_] + weight
            min_cycle = min(min_cycle, cycle_len)


if min_dist == INF :
    print(-1)
else:
    print(min_dist)