# bfs dfs

n,m,v = map(int,input().split())
visited = [ False for _ in range(n+1)]
graph=[[] for _ in range(n+1)]

for i in range(1,m+1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

def dfs(start):
    print(start, end = ' ')
    visited[start] = True
    
    for x in graph[start]:
        if not visited[x]:
            dfs(x)
        
        
dfs(v)