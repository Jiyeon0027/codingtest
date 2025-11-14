from collections import deque

# dfs 재귀방식
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q= deque()
    q.append(v)
    visited[v] = True
    # print(q.popleft())
    while q:
        cur = q.popleft()
        print(cur, end =' ')
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

# dfs(graph, 1, visited)
# bfs(graph, 1, visited)