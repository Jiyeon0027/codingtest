#트리의 지름
# dijkstra

import sys
from heapq import heappop, heappush
input= sys.stdin.readline
sys.setrecursionlimit(10**6)
# graph=[]
map_graph={}

n = int(input())

for _ in range(n-1):
    pr, ch, weight = map(int, input().strip().split())
    if pr not in map_graph:
        map_graph[pr] = []
    if ch not in map_graph:
        map_graph[ch] = []
    map_graph[pr].append((ch,weight))
    map_graph[ch].append((pr,weight))
    # graph.append([weight,pr,ch,False])
# print(graph)

def dfs (start, dist):
    if start not in map_graph:
        return
    for i,w in map_graph[start]:
        if visited[i] == -1: #방문하지 않았을 경우에
            visited[i] = dist + w
            dfs(i,dist+w)
        
visited = [-1 for _ in range(n+1)]
visited[1] = 0 
dfs(1,0)
# print(visited)
max_distance = max(visited)
max_node= visited.index(max_distance)

visited = [-1 for _ in range(n+1)]
visited[max_node] = 0
dfs(max_node, 0)
# print(visited)

print(max(visited))

# graph.sort(key= lambda x : -x[0])
# print(graph)


# def dijkstra(start):
#     hq =[]
#     max_dist = 0
#     x = graph[start]
#     graph[start][3] = False #방문 완료
#     heappush(hq,(-x[0], x[1], x[2], x[3]))
#     max_dist += x[0]
#     while hq:
#         cur_w, v1 ,v2, _ = heappop(hq)
#         idx =-1
#         for nxt_node, nxt_w in map_graph[v1]:
            
            
# # def floid(): 1_000_000_000_000
# #     for i in range(n):
# #         for j in range(n):
# #             for k in range(n)

# dijkstra(0)