# 위상 정렬 - 방향성을 거스르지 않도록 정렬 하는 것

from collections import deque

v, e = map(int,input().split())
indegree = [0 for _ in range(v+1)]
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
    
    return result

print(topology_sort())