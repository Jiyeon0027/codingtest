from collections import deque

dir = [(1,0), (-1,0), (0,1), (0,-1)]

n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)] 

for i in range(n):
    graph.append(list(map(int,input().strip())))
    
    
q = deque()
q.append([0,0])
visited[0][0] = 1 #시작
while q:
    # print(q)
    x,y = q.popleft()
    
    for dx, dy in dir:
        cx , cy = x+dx, y+dy
        
        if cx < 0 or cx >= n or cy<0 or cy>=m : 
            continue
        
        if graph[cx][cy] == 0: #괴물이 있는 부분
            continue
        
        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if visited[cx][cy] == 0 or visited[cx][cy] >  visited[x][y] + 1:
            visited[cx][cy] = visited[x][y] + 1
            # print(*visited, sep = '\n')
            q.append([cx,cy])
        
        
print(visited[n-1][m-1])